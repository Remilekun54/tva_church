from django.db import models
from django.utils.text import slugify

class Department(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto-generated from name")
    
    # List Page Fields
    card_image = models.ImageField(upload_to='departments/cards/', help_text="Image displayed on the department list.")
    card_summary = models.TextField(help_text="Short description for the card overview.")
    
    # Detail Page Fields
    hero_image = models.ImageField(upload_to='departments/heroes/', help_text="Large banner image for the department detail page.")
    content = models.TextField(help_text="Full details about the department (History, activities, etc.)")
    
    order = models.PositiveIntegerField(default=0, help_text="Order in the list (lowest first)")
    
    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
