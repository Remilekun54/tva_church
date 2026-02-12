from django.contrib import admin
import datetime
from .models import Sermon, Book, SermonCategory

@admin.register(SermonCategory)
class SermonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ('title', 'category', 'preacher', 'branch', 'date_preached', 'status', 'is_trending')
    
    # Filtering options
    list_filter = ('category', 'status', 'branch', 'is_trending', 'date_preached')
    
    # Search box
    search_fields = ('title', 'theme', 'series_name', 'description', 'preacher__name')
    
    # Quick edits
    list_editable = ('status', 'is_trending')
    
    # Field groupings
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'theme', 'series_name', 'description', 'thumbnail')
        }),
        ('Pricing', {
            'fields': ('status', 'price') 
        }),
        ('External Links', {
            'fields': ('video_url', 'audio_url')
        }),
        ('Direct Uploads', {
            'fields': ('video_file', 'audio_file')
        }),
        ('Details & Relationships', {
            'fields': ('preacher', 'branch', 'duration', 'date_preached')
        }),
        ('Visibility', {
            'fields': ('is_trending',)
        }),
    )

    def get_changeform_initial_data(self, request):
        return {'date_preached': datetime.date.today()}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'price', 'book_type', 'created_at')
    list_filter = ('status', 'book_type', 'author')
    search_fields = ('title', 'author', 'description')
    list_editable = ('status', 'price')
    
    fieldsets = (
        ('Book Details', {
            'fields': ('title', 'author', 'book_type', 'description', 'thumbnail', 'pages')
        }),
        ('Pricing & Access', {
            'fields': ('status', 'price', 'pdf_file', 'external_purchase_link')
        }),
    )