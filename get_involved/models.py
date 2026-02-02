from django.db import models
from django.core.exceptions import ValidationError

class MembershipPathwayPage(models.Model):
    """Singleton model for the Membership Pathway Page Config"""
    hero_title = models.CharField(max_length=200, default="Membership Pathway")
    hero_subtitle = models.CharField(max_length=200, default="Your Journey to Belonging")
    hero_image = models.ImageField(upload_to='get_involved/', blank=True, null=True)
    
    intro_title = models.CharField(max_length=200, default="Discovery Track")
    intro_description = models.TextField(default="We want to help you connect, grow, and serve.")

    def save(self, *args, **kwargs):
        if not self.pk and MembershipPathwayPage.objects.exists():
            raise ValidationError('There can be only one Membership Pathway Page instance')
        return super(MembershipPathwayPage, self).save(*args, **kwargs)

    def __str__(self):
        return "Membership Pathway Page Configuration"

    class Meta:
        verbose_name = "Page Configuration"
        verbose_name_plural = "Page Configuration"


class PathwayStep(models.Model):
    """Six steps of membership"""
    page = models.ForeignKey(MembershipPathwayPage, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField(unique=True, help_text="1 to 6")
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g., 'heart', 'users', 'check-circle')", default="circle")
    
    # Optional image if they prefer images over icons for some steps
    image = models.ImageField(upload_to='get_involved/steps/', blank=True, null=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"

from departments.models import Department

class ChurchMembershipRegistration(models.Model):
    """Model for general church membership registration"""
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    how_did_you_hear = models.CharField(max_length=200, blank=True, verbose_name="How did you hear about us?")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Member Registration: {self.full_name}"

class DepartmentRegistration(models.Model):
    """Model for joining a specific department"""
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, help_text="Select the department you wish to join")
    reason_for_joining = models.TextField(verbose_name="Why do you want to join this department?")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} -> {self.department.name if self.department else 'Unknown'}"

class CityAltar(models.Model):
    """Model for House Fellowships / City Altars"""
    name = models.CharField(max_length=200, help_text="Name of the City Altar location")
    image = models.ImageField(upload_to='get_involved/city_altars/', blank=True, null=True)
    leader_name = models.CharField(max_length=200)
    address = models.TextField()
    location = models.CharField(max_length=100, help_text="City or Area (e.g., Ikeja, Lekki)")
    
    MEETING_DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    meeting_day = models.CharField(max_length=20, choices=MEETING_DAYS, default='Tuesday')
    meeting_time = models.TimeField()
    
    description = models.TextField(blank=True, help_text="Brief description or welcome message")
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.location})"

    class Meta:
        verbose_name = "City Altar / House Fellowship"
        verbose_name_plural = "City Altars / House Fellowships"

class Fellowship(models.Model):
    """Model for different fellowships (Box-18, V-Mums, Singles)"""
    FELLOWSHIP_Types = [
        ('BOX18', 'Box-18 (Men)'),
        ('VMUMS', 'V-Mums (Women)'),
        ('SINGLES', 'Singles & Youths'),
    ]
    
    name = models.CharField(max_length=20, choices=FELLOWSHIP_Types, unique=True)
    hero_image = models.ImageField(upload_to='fellowships/', blank=True, null=True, help_text="Main banner image for the page")
    
    about_title = models.CharField(max_length=200, default="About Us")
    about_text = models.TextField(help_text="Detailed information about the fellowship")
    
    activities_summary = models.TextField(help_text="Overview of activities for the year", blank=True)
    calendar_file = models.FileField(upload_to='fellowships/calendars/', blank=True, null=True, help_text="Upload calendar PDF or image")
    
    join_info = models.TextField(help_text="Instructions on how new members can join")
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name_display()

class FellowshipEvent(models.Model):
    """Events specific to a fellowship"""
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='fellowships/events/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} ({self.date})"
    
    class Meta:
        ordering = ['-date']

# Proxy models for separate Admin sections
class Box18Fellowship(Fellowship):
    class Meta:
        proxy = True
        verbose_name = "Box-18 (Men's Fellowship)"
        verbose_name_plural = "Box-18 (Men's Fellowship)"

class VMumsFellowship(Fellowship):
    class Meta:
        proxy = True
        verbose_name = "V-Mums (Women's Fellowship)"
        verbose_name_plural = "V-Mums (Women's Fellowship)"

class SinglesFellowship(Fellowship):
    class Meta:
        proxy = True
        verbose_name = "Singles & Youths"
        verbose_name_plural = "Singles & Youths"
