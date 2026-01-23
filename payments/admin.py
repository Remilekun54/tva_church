from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BankDetail

@admin.register(BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'account_name', 'is_active')