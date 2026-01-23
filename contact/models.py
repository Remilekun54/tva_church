from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
from django.db import models

class Branch(models.Model):
    branch_name = models.CharField(max_length=100, default="The Sanctuary")
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name_plural = "Branches"