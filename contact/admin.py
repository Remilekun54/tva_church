from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    # This controls what columns you see in the list view
    list_display = ('name', 'email', 'created_at')
    
    # This adds a filter sidebar on the right to sort by date
    list_filter = ('created_at',)
    
    # This adds a search bar to find messages by name or email
    search_fields = ('name', 'email', 'message')
    
    # This makes the fields "Read Only" so the admin doesn't change the user's message
    readonly_fields = ('name', 'email', 'message', 'created_at')

    # This prevents the "Add" button from appearing in the Admin Dashboard
    def has_add_permission(self, request):
        return False
    

from django.contrib import admin
from .models import Branch, ContactMessage

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'email')

# Keep your ContactMessage registration here as well