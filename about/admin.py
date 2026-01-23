from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AboutSection
from .models import Branch, BranchActivity
from .models import CoreValue
from .models import Leader


@admin.register(AboutSection)
class AboutAdmin(admin.ModelAdmin):
    # This prevents the admin from adding multiple about sections
    def has_add_permission(self, request):
        if AboutSection.objects.exists():
            return False
        return True
    

class ActivityInline(admin.TabularInline):
    model = BranchActivity
    extra = 1 # Shows one empty row by default

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


from django.contrib import admin
from .models import AboutSection, StatementOfFaith, BeliefPoint

# 1. Register the Statement of Faith Header
@admin.register(StatementOfFaith)
class StatementOfFaithAdmin(admin.ModelAdmin):
    list_display = ('sof_title', 'sof_subtitle')
    
    # This prevents the "Add" button from showing up if an entry already exists
    def has_add_permission(self, request):
        if StatementOfFaith.objects.exists():
            return False
        return True

# 2. Register the individual Belief Points
@admin.register(BeliefPoint)
class BeliefPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


from .models import HistoryMilestone

@admin.register(HistoryMilestone)
class HistoryMilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order')
    list_editable = ('order',)

from .models import Statistic

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'order')
    list_editable = ('order',)