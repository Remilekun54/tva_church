from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from about.models import Branch, Leader

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