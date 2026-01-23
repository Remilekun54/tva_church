from django.db import models

# Create your models here.
from django.db import models

class BankDetail(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    account_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True, help_text="Uncheck this to hide these details site-wide")

    class Meta:
        verbose_name = "Church Bank Detail"

    def __str__(self):
        return f"{self.bank_name} - {self.account_name}"