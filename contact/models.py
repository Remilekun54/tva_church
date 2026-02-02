from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
from django.db import models

class Branch(models.Model):
    branch_name = models.CharField(max_length=100, default="The Sanctuary")
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name_plural = "Branches"


class Testimony(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    testimony_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimony from {self.name}"
    
    class Meta:
        verbose_name_plural = "Testimonies"


class ContactPageSettings(models.Model):
    facebook = models.URLField(blank=True, null=True, help_text="Facebook Page URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")
    mixlr = models.URLField(blank=True, null=True, help_text="Mixlr URL")
    telegram = models.URLField(blank=True, null=True, help_text="Telegram Channel URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram Profile URL")
    x_twitter = models.URLField(blank=True, null=True, verbose_name="X (Twitter)", help_text="X (Twitter) Profile URL")
    
    # Social Media Section Text
    social_media_section_title = models.CharField(max_length=100, default="Connect With Us", help_text="Small title above the heading")
    social_media_section_heading = models.CharField(max_length=200, default="Join Our Online Community", help_text="Main heading")
    social_media_section_description = CKEditor5Field('Content', config_name='default', default="Stay connected with TVA on social media. Follow us for live updates, sermons, and daily inspiration.")

    # Google Map
    google_map_embed = models.TextField(blank=True, null=True, help_text="Paste the Google Maps Embed HTML code here (iframe)")
    google_map_link = models.URLField(blank=True, null=True, help_text="Link to open location in Google Maps (optional)")

    # Testimony Section Text
    testimony_section_title = models.CharField(max_length=100, default="Share Your Story", help_text="Small title above the heading")
    testimony_section_heading = models.CharField(max_length=200, default="Has God been good to you?", help_text="Main heading")
    testimony_section_description = CKEditor5Field('Content', config_name='default', default="Your testimony can be the key to someone else's breakthrough. Share what the Lord has done in your life.")

    class Meta:
        verbose_name = "Contact Page Settings"
        verbose_name_plural = "Contact Page Settings"

    def __str__(self):
        return "Contact Page Configuration"