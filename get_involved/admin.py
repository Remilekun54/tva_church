from django.contrib import admin
from .models import MembershipPathwayPage, PathwayStep, ChurchMembershipRegistration, DepartmentRegistration, CityAltar

@admin.register(CityAltar)
class CityAltarAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'leader_name', 'whatsapp_number', 'meeting_day', 'meeting_time')
    search_fields = ('name', 'location', 'leader_name', 'address')
    list_filter = ('meeting_day', 'location')

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

from .models import Box18Fellowship, VMumsFellowship, SinglesFellowship, FellowshipEvent, Fellowship

class FellowshipEventInline(admin.StackedInline):
    model = FellowshipEvent
    extra = 1
    classes = ('collapse',)

class BaseFellowshipAdmin(admin.ModelAdmin):
    inlines = [FellowshipEventInline]
    exclude = ('name',) # Name is set automatically
    
    def has_add_permission(self, request):
        # Only allow one instance per type
        if self.model.objects.filter(name=self.expected_type).exists():
            return False
        return True

    def get_queryset(self, request):
        return super().get_queryset(request).filter(name=self.expected_type)

    def save_model(self, request, obj, form, change):
        obj.name = self.expected_type
        super().save_model(request, obj, form, change)

@admin.register(Box18Fellowship)
class Box18Admin(BaseFellowshipAdmin):
    expected_type = 'BOX18'

@admin.register(VMumsFellowship)
class VMumsAdmin(BaseFellowshipAdmin):
    expected_type = 'VMUMS'

@admin.register(SinglesFellowship)
class SinglesAdmin(BaseFellowshipAdmin):
    expected_type = 'SINGLES'

from .models import G12Page, G12Registration

@admin.register(G12Page)
class G12PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True
    
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('Section 1', {
            'fields': ('section1_title', 'section1_content', 'section1_image')
        }),
        ('Section 2', {
            'fields': ('section2_title', 'section2_content', 'section2_image')
        }),
        ('Section 3', {
            'fields': ('section3_title', 'section3_content', 'section3_image')
        }),
        ('Registration Section', {
            'fields': ('registration_title', 'registration_subtitle')
        }),
    )

@admin.register(G12Registration)
class G12RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'branch', 'created_at')
    list_filter = ('branch', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number')
    readonly_fields = ('created_at',)
