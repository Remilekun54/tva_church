from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventCategory, EventRegistration

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_open_event', 'status_badge', 'is_active')
    list_filter = ('category', 'is_open_event', 'date', 'is_active')
    list_editable = ('is_open_event', 'is_active')
    search_fields = ('title', 'location', 'description')

    def status_badge(self, obj):
        if obj.is_open:
            return format_html('<span style="background:#10b981;color:#fff;padding:3px 8px;border-radius:12px;font-weight:bold;font-size:11px;">Open Event</span>')
        return format_html('<span style="background:#ef4444;color:#fff;padding:3px 8px;border-radius:12px;font-weight:bold;font-size:11px;">Closed Event</span>')
    status_badge.short_description = 'Open/Closed'


from .models import Event, EventRegistration

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'event', 'email', 'phone_number', 'registration_date')
    list_filter = ('event', 'registration_date')
    search_fields = ('full_name', 'email')