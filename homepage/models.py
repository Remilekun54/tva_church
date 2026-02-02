

# Create your models here.

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Hero Slide Model
class HeroSlide(models.Model):
    title = models.CharField(max_length=200, help_text="Use <br> for line breaks and <span class='text-secondary italic'>Text</span> for gold text")
    sub_heading = models.CharField(max_length=100)
    description = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='hero_slides/')
    live_stream_button_text = models.CharField(max_length=50, blank=True, null=True, default="Watch Live", help_text="Text for the live stream button")
    live_stream_url = models.URLField(blank=True, null=True, help_text="URL for the live stream (e.g., YouTube Link). Leave empty to hide button.")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
# About Section Model
class AboutSection(models.Model):
    tagline = models.CharField(max_length=100, default="About Us")
    title = models.CharField(max_length=255, help_text="Use <br> for line breaks and <span class='text-secondary italic'>Text</span> for styled text")
    description = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='about_section/')
    button_text = models.CharField(max_length=50, default="Discover Our Mission")
    button_url = models.CharField(max_length=255, default="/about/")

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

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


# Core Value Model
class CoreValue(models.Model):
    title = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=50, help_text="Enter Lucide icon name (e.g., flame, book-open, users)")
    description = CKEditor5Field('Content', config_name='default')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title


# Store Section Model
class StoreSection(models.Model):
    subtitle = models.CharField(max_length=100, default="Our Store")
    title = models.CharField(max_length=255, help_text="Use <br> for line breaks and <span class='text-secondary italic'>Text</span> for styled text")
    description = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='store_section/')
    
    # Feature 1
    feature1_title = models.CharField(max_length=100, default="Books")
    feature1_text = models.CharField(max_length=255, default="In-depth study guides")
    
    # Feature 2
    feature2_title = models.CharField(max_length=100, default="Courses/Apparel")
    feature2_text = models.CharField(max_length=255, default="TVA Merchandise")
    
    button_text = models.CharField(max_length=50, default="Visit the Store")
    button_url = models.CharField(max_length=255, default="/store/")

    class Meta:
        verbose_name = "Store Section"
        verbose_name_plural = "Store Section"

    def __str__(self):
        return self.title

from django.db import models


# Footer Settings Model
class FooterSettings(models.Model):
    tagline = models.TextField(default='"A garden where souls are nurtured by grace..."')
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    copyright_text = models.CharField(max_length=255, default="The Vineyard Assembly. All rights reserved.")

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


# Pastor Section Model
class PastorSection(models.Model):
    tagline = models.CharField(max_length=100, default="Our Shepherd")
    name = models.CharField(max_length=255, default="Pastor Adeyinka")
    quote = models.TextField(help_text="The italicized quote")
    description = CKEditor5Field('Content', config_name='default', help_text="The main bio description")
    image = models.ImageField(upload_to='pastor_section/')
    button_text = models.CharField(max_length=100, default="Read Full Bio")
    button_url = models.CharField(max_length=255, default="/about/")

    class Meta:
        verbose_name = "Pastor Section"
        verbose_name_plural = "Pastor Section"

    def __str__(self):
        return self.name

# Featured Quote Model
class FeaturedQuote(models.Model):
    quote = models.TextField()
    author_label = models.CharField(max_length=100, default="TVA Mandate")

    class Meta:
        verbose_name = "Featured Quote"
        verbose_name_plural = "Featured Quote"

    def __str__(self):
        return self.author_label

# Giving Section Model
class GivingSection(models.Model):
    title = models.CharField(max_length=255, default="Partner with the Vision")
    description = CKEditor5Field('Content', config_name='default')
    button_text = models.CharField(max_length=100, default="Give Online")
    button_url = models.CharField(max_length=255, default="/offering/")

    class Meta:
        verbose_name = "Giving Section"
        verbose_name_plural = "Giving Section"

    def __str__(self):
        return self.title

# Events Header Model
class EventsHeader(models.Model):
    title = models.CharField(max_length=255, default="Upcoming Events & News")

    class Meta:
        verbose_name = "Events Header"
        verbose_name_plural = "Events Header"

    def __str__(self):
        return self.title