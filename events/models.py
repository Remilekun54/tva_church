
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    tagline = models.CharField(max_length=100, help_text="e.g., Special Encounter")
    description = CKEditor5Field('Content', config_name='default', help_text="Brief description of the event")
    image = models.ImageField(upload_to='events/')
    
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.CharField(max_length=255)
    
    registration_url = models.URLField(blank=True, help_text="Link to external form or internal page")
    button_text = models.CharField(max_length=50, default="Register Now")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time_start']

    def __str__(self):
        return self.title
    
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.event.title}"