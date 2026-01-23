from django.contrib import admin
from .models import Event, EventCategory

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_active')
    list_filter = ('category', 'date', 'is_active')
    search_fields = ('title', 'location', 'description')


from .models import Event, EventRegistration

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'event', 'email', 'phone_number', 'registration_date')
    list_filter = ('event', 'registration_date')
    search_fields = ('full_name', 'email')