

# Create your models here.

from django.db import models

# Hero Slide Model
class HeroSlide(models.Model):
    title = models.CharField(max_length=200, help_text="Use <br> for line breaks and <span class='text-secondary italic'>Text</span> for gold text")
    sub_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_slides/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
# Sermon Model

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)  # e.g., Foundations, Grace
    image = models.ImageField(upload_to='sermons/')
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    video_url = models.URLField(blank=True, null=True, help_text="Link to the sermon video")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date'] # Show newest first

    def __str__(self):
        return self.title
    

# Event Model

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(help_text="Short summary of the event")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date'] # Shows soonest events first

    def __str__(self):
        return self.title
    


# Gallery Image Model
class GalleryImage(models.Model):
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption for the image")
    image_file = models.ImageField(upload_to='gallery/', blank=True, null=True, help_text="Upload an image from your computer")
    external_url = models.URLField(blank=True, null=True, help_text="Or paste a link from the internet (e.g., Unsplash)")
    order = models.PositiveIntegerField(default=0, help_text="Order to display images")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption or f"Gallery Image {self.id}"

    @property
    def image_url(self):
        if self.image_file:
            return self.image_file.url
        return self.external_url
    

# Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

from django.db import models


# Footer Settings Model
class FooterSettings(models.Model):
    tagline = models.TextField(default='"A garden where souls are nurtured by grace..."')
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    copyright_text = models.CharField(max_length=255, default="Garden of Grace and Prayer Sanctuary. All rights reserved.")

    class Meta:
        verbose_name = "Footer Setting"

# Church Branch Model
class ChurchBranch(models.Model):
    branch_name = models.CharField(max_length=100, help_text="e.g., Main Sanctuary or North Branch")
    sunday_service_1 = models.CharField(max_length=100, default="Empowerment: 8:00 AM")
    sunday_service_2 = models.CharField(max_length=100, default="Celebration: 10:30 AM")
    midweek_service = models.CharField(max_length=100, default="Wednesday Word: 6:00 PM")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Church Branches"
        ordering = ['order']

    def __str__(self):
        return self.branch_name