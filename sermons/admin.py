from django.contrib import admin
import datetime
from .models import Sermon, Book

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ('title', 'preacher', 'branch', 'date_preached', 'status', 'price', 'is_trending')
    
    # Filtering options
    list_filter = ('status', 'branch', 'is_trending', 'date_preached')
    
    # Search box
    search_fields = ('title', 'series_name', 'description', 'preacher__name')
    
    # Quick edits
    list_editable = ('status', 'is_trending', 'price')
    
    # Field groupings
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'series_name', 'description', 'thumbnail')
        }),
        ('Pricing', {
            # REMOVE 'store_url' FROM HERE
            'fields': ('status', 'price') 
        }),
        ('Media Links', {
            'fields': ('video_url', 'audio_url')
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