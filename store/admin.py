from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'product_type', 'is_active')
    list_filter = ('category', 'product_type', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('price', 'is_active')