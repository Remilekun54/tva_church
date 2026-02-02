from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPES = [
        ('digital', 'Digital (Downloadable)'),
        ('physical', 'Physical (Shippable)'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Content', config_name='default')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='store/thumbnails/')
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPES, default='physical')
    
    # Optional fields for specific items
    author_or_preacher = models.CharField(max_length=255, blank=True, help_text="Optional: Name of Author/Preacher")
    file_upload = models.FileField(upload_to='store/digital/', blank=True, null=True, help_text="For digital books/audio")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title