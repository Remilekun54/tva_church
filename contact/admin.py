from django.contrib import admin
from .models import ContactMessage, Branch, Testimony, ContactPageSettings

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def has_add_permission(self, request):
        return False

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'email')

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)

@admin.register(ContactPageSettings)
class ContactPageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social Media Links', {
            'fields': ('facebook', 'youtube', 'instagram', 'x_twitter', 'telegram', 'mixlr')
        }),
        ('Social Media Section Content', {
            'fields': ('social_media_section_title', 'social_media_section_heading', 'social_media_section_description'),
            'description': 'Customize the text displayed in the Social Media section.'
        }),
        ('Google Map', {
            'fields': ('google_map_embed', 'google_map_link')
        }),
        ('Testimony Section Content', {
            'fields': ('testimony_section_title', 'testimony_section_heading', 'testimony_section_description'),
            'description': 'Customize the text displayed in the Testimony section.'
        }),
    )

    def has_add_permission(self, request):
        # Only allow 1 instance
        return not ContactPageSettings.objects.exists()