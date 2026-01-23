
# Register your models here.
from django.contrib import admin
from .models import HeroSlide
from .models import Sermon
from .models import Event
from .models import GalleryImage
from .models import ContactMessage 
from .models import FooterSettings, ChurchBranch


# Hero Slide Admin
@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')

# Sermon Admin
@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'duration')
    list_filter = ('category', 'date')
    search_fields = ('title', 'category')


# Event Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)


# Gallery Image Admin


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order', 'image_file', 'external_url')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at') # Prevent admin from editing user messages
    search_fields = ('name', 'email')


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    # Only allow one instance of settings
    def has_add_permission(self, request):
        return not FooterSettings.objects.exists()

@admin.register(ChurchBranch)
class ChurchBranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'order')
    list_editable = ('order',)