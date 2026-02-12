# Register your models here.
from django.contrib import admin
from .models import HeroSlide, AboutSection, CoreValue, StoreSection, PastorSection, FeaturedQuote, GivingSection, EventsHeader
from .models import GalleryImage
from .models import ContactMessage 
from .models import FooterSettings, ChurchBranch


# Hero Slide Admin
@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')

# About Section Admin
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutSection.objects.exists()



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


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order')
    list_editable = ('order',)

@admin.register(StoreSection)
class StoreSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not StoreSection.objects.exists()

@admin.register(PastorSection)
class PastorSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'order')
    list_editable = ('order',)

@admin.register(FeaturedQuote)
class FeaturedQuoteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not FeaturedQuote.objects.exists()

@admin.register(GivingSection)
class GivingSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not GivingSection.objects.exists()

@admin.register(EventsHeader)
class EventsHeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not EventsHeader.objects.exists()