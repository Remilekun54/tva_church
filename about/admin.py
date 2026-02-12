from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AboutSection, BeliefPoint, Branch, BranchActivity, CoreValue, Leader, HistoryMilestone, Statistic
from .models import FoundingPastor, PresidingPastor, PastoralTeam, PastoralTimeline, TeamMember


class BeliefPointInline(admin.TabularInline):
    model = BeliefPoint
    extra = 3
    fields = ('title', 'description', 'order')
    classes = ('collapse',)

@admin.register(AboutSection)
class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Story & Foundation', {
            'fields': ('subtitle', 'title', 'main_image', 'established_year', 'established_text', 'foundation_quote', 'description')
        }),
        ('Mission & Vision', {
            'fields': ('mission_subtitle', 'mission_title', 'mission_description', 'vision_title', 'vision_description')
        }),
        ('Statement of Faith & Doctrine Upload', {
            'fields': ('sof_subtitle', 'sof_title', 'sof_description', 'doctrine_pdf'),
            'description': 'Manage the Statement of Faith and upload the Doctrine PDF here.'
        }),
    )
    inlines = [BeliefPointInline]

    def has_add_permission(self, request):
        if AboutSection.objects.exists():
            return False
        return True

class ActivityInline(admin.TabularInline):
    model = BranchActivity
    extra = 1

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'is_active')
    inlines = [ActivityInline]

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'color_scheme')
    list_editable = ('order', 'color_scheme')

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'branch', 'order')
    list_editable = ('order', 'branch')
    list_filter = ('branch',)
    fields = ('name', 'position', 'branch', 'image', 'contact_email', 'facebook_url', 'instagram_url', 'linkedin_url', 'tiktok_url', 'order')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'pastoral_team', 'order')
    list_editable = ('order',)
    list_filter = ('pastoral_team',)

@admin.register(BeliefPoint)
class BeliefPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

# Additional models registered below

@admin.register(HistoryMilestone)
class HistoryMilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order')
    list_editable = ('order',)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'order')
    list_editable = ('order',)

# Pastoral Pages Admin

class PastoralTimelineInline(admin.TabularInline):
    model = PastoralTimeline
    extra = 2
    fields = ('year', 'title', 'description', 'order')

@admin.register(FoundingPastor)
class FoundingPastorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('Biography Section', {
            'fields': ('bio_title', 'bio_content', 'bio_image')
        }),
        ('Vision Section', {
            'fields': ('vision_title', 'vision_content', 'vision_image')
        }),
        ('Legacy Section', {
            'fields': ('legacy_title', 'legacy_content', 'legacy_image')
        }),
        ('Quotes Section', {
            'fields': ('quotes_title', 'featured_quote', 'quote_author', 'quote_image')
        }),
        ('Timeline Section', {
            'fields': ('timeline_title', 'timeline_image')
        }),
        ('Contact & Social Section', {
            'fields': ('contact_title', 'contact_email', 'facebook_url', 'instagram_url', 'linkedin_url', 'mixlr_url', 'threads_url', 'x_url', 'tiktok_url')
        }),
        ('Books Section', {
            'fields': ('books_title', 'selar_book_url', 'amazon_book_url', 'medium_url')
        }),
    )
    inlines = [PastoralTimelineInline]
    
    def has_add_permission(self, request):
        return not FoundingPastor.objects.exists()

@admin.register(PresidingPastor)
class PresidingPastorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image', 'pastor_name')
        }),
        ('Biography Section', {
            'fields': ('bio_title', 'bio_content', 'bio_image')
        }),
        ('Vision Section', {
            'fields': ('vision_title', 'vision_content', 'vision_image')
        }),
        ('Ministry Focus Section', {
            'fields': ('focus_title', 'focus_content', 'focus_image')
        }),
        ('Message Section', {
            'fields': ('message_title', 'message_content', 'message_image')
        }),
        ('Contact Section', {
            'fields': ('contact_title', 'contact_email', 'facebook_url', 'instagram_url', 'linkedin_url', 'mixlr_url', 'threads_url', 'x_url', 'tiktok_url')
        }),
        ('Books Section', {
            'fields': ('books_title', 'selar_book_url', 'amazon_book_url', 'medium_url')
        }),
    )
    
    def has_add_permission(self, request):
        return not PresidingPastor.objects.exists()

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 3
    fields = ('name', 'position', 'ministry_area', 'bio', 'image', 'contact_email', 'facebook_url', 'instagram_url', 'linkedin_url', 'tiktok_url', 'order')

@admin.register(PastoralTeam)
class PastoralTeamAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('Overview Section', {
            'fields': ('overview_title', 'overview_content', 'overview_image')
        }),
        ('Structure Section', {
            'fields': ('structure_title', 'structure_content', 'structure_image')
        }),
        ('Values Section', {
            'fields': ('values_title', 'values_content', 'values_image')
        }),
        ('Ministry Areas Section', {
            'fields': ('ministry_title',)
        }),
        ('Join Team Section', {
            'fields': ('join_title', 'join_content', 'join_image')
        }),
    )
    inlines = [TeamMemberInline]
    
    def has_add_permission(self, request):
        return not PastoralTeam.objects.exists()
