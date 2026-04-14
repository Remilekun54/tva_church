from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from about.models import Branch, Leader
import uuid

class CommonBase(models.Model):
    """Abstract base to keep code clean and shared between Sermons and Books"""
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid/Buy'),
    ]
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Content', config_name='default')
    thumbnail = models.ImageField(upload_to='resources/thumbnails/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class SermonCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Sermon Categories"

    def __str__(self):
        return self.name

class Sermon(CommonBase):
    category = models.ForeignKey(SermonCategory, on_delete=models.SET_NULL, null=True, blank=True)
    theme = models.CharField(max_length=255, blank=True, help_text="The theme of the sermon/series")
    series_name = models.CharField(max_length=100, blank=True, help_text="e.g., The Overflow Series")
    
    video_url = models.URLField(blank=True, help_text="YouTube link (optional if uploading video)")
    video_file = models.FileField(upload_to='sermons/videos/', blank=True, null=True, help_text="Upload video file if not using YouTube")
    
    audio_url = models.URLField(blank=True, help_text="Telegram audio link (optional if uploading audio)")
    audio_file = models.FileField(upload_to='sermons/audios/', blank=True, null=True, help_text="Upload audio file for direct download")
    
    preacher = models.ForeignKey(Leader, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    duration = models.CharField(max_length=20, help_text="e.g., 45 Mins")
    date_preached = models.DateField()
    is_trending = models.BooleanField(default=False)
    is_live_recording = models.BooleanField(
        default=False,
        help_text="Automatically set to True when created from a live broadcast recording."
    )

    class Meta:
        ordering = ['-date_preached']

    def __str__(self):
        return self.title

class Book(CommonBase):
    BOOK_TYPES = [
        ('ebook', 'E-Book (Digital)'),
        ('physical', 'Physical Copy'),
    ]
    author = models.CharField(max_length=255, default="GOGAP Publications")
    book_type = models.CharField(max_length=20, choices=BOOK_TYPES, default='ebook')
    pages = models.PositiveIntegerField(blank=True, null=True)
    
    # For free books, allow direct upload
    pdf_file = models.FileField(upload_to='books/pdfs/', blank=True, null=True, help_text="Upload PDF if the book is free")
    
    # If the book is sold elsewhere
    external_purchase_link = models.URLField(blank=True, help_text="Link to Amazon/Other store")

    def __str__(self):
        return self.title


class AudioBroadcast(models.Model):
    """
    Represents a single live audio broadcast session.
    OBS streams via RTMP to a media server; this model stores the HLS
    playback URL and controls whether the 'Listen Live' player is shown.
    """
    title = models.CharField(max_length=255, help_text="e.g., Sunday Celebration Service")
    preacher = models.ForeignKey(
        Leader, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Who is preaching this session?"
    )
    stream_key = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True,
        help_text="Auto-generated. Use this as your OBS stream key."
    )
    hls_stream_url = models.URLField(
        blank=True,
        help_text="Paste your HLS stream URL (.m3u8) from your media server (nginx-rtmp, Cloudflare, etc.)"
    )
    is_live = models.BooleanField(
        default=False,
        help_text="Toggle ON to start broadcasting. The 'Listen Live' player will appear on the site."
    )
    last_broadcast_end = models.DateTimeField(
        null=True, blank=True,
        help_text="Automatically set when you toggle 'is_live' off."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Audio Broadcast"
        verbose_name_plural = "Audio Broadcasts"
        ordering = ['-created_at']

    def __str__(self):
        status = "LIVE" if self.is_live else "Offline"
        return f"{self.title} - {status}"

    def save(self, *args, **kwargs):
        """
        Custom save to handle broadcast lifecycle events:
        1. Set last_broadcast_end when ending a stream.
        2. Auto-create a Sermon entry for the archives.
        """
        if self.pk:
            # Check if this is a transition from LIVE to OFFLINE
            try:
                old_instance = AudioBroadcast.objects.get(pk=self.pk)
                if old_instance.is_live and not self.is_live:
                    from django.utils import timezone
                    self.last_broadcast_end = timezone.now()
                    
                    # Create the archived Sermon record
                    from .models import Sermon
                    
                    Sermon.objects.create(
                        title=self.title,
                        preacher=self.preacher,
                        date_preached=timezone.localdate(),
                        is_live_recording=True,
                        description=f"Recorded broadcast from {timezone.localdate()}",
                        # Admin can update audio_file / thumbnail / category later
                    )
            except AudioBroadcast.DoesNotExist:
                pass

        super().save(*args, **kwargs)