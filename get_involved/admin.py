from django.contrib import admin
from .models import MembershipPathwayPage, PathwayStep, ChurchMembershipRegistration, DepartmentRegistration

@admin.register(ChurchMembershipRegistration)
class ChurchMembershipRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'gender', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('gender', 'created_at')

@admin.register(DepartmentRegistration)
class DepartmentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'department', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('department', 'created_at')

class PathwayStepInline(admin.StackedInline):
    model = PathwayStep
    extra = 1
    max_num = 6 # Limit to 6 steps as requested
    fields = ('step_number', 'title', 'description', 'icon_name', 'image')

@admin.register(MembershipPathwayPage)
class MembershipPathwayPageAdmin(admin.ModelAdmin):
    inlines = [PathwayStepInline]
    
    def has_add_permission(self, request):
        # Only allow creating one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('Intro Section', {
            'fields': ('intro_title', 'intro_description')
        }),
    )
