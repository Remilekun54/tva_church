from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sellar_price', 'amazon_price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('sellar_price', 'amazon_price', 'is_active')