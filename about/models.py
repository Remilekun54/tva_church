from django.db import models

class AboutSection(models.Model):
    # Header Section
    title = models.CharField(max_length=200, default="Our Story & Vision")
    subtitle = models.CharField(max_length=100, default="Who We Are")
    main_image = models.ImageField(upload_to='about/', null=True, blank=True)
    established_year = models.CharField(max_length=20, default="Est. 2012")
    established_text = models.CharField(max_length=100, default="A Decade of Grace")
    description = models.TextField(default="")
    
    # Mission Section
    mission_subtitle = models.CharField(max_length=100, default="Our Purpose")
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_description = models.TextField(default="To cultivate a global garden...")

    # Vision Section
    vision_subtitle = models.CharField(max_length=100, default="Our Future")
    vision_title = models.CharField(max_length=100, default="Our Vision")
    vision_description = models.TextField(default="To see the fragrance of God's presence...")

    class Meta:
        verbose_name_plural = "About Section"

    def __str__(self):
        return "About Page Content"

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    location_label = models.CharField(max_length=255, default="Global Grace Headquarters")
    address_url = models.URLField(help_text="Google Maps link", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.branch_name

class BranchActivity(models.Model):
    branch = models.ForeignKey(Branch, related_name='activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="e.g., Sunday Service or Midweek Service")
    time_slots = models.TextField(help_text="Enter times, one per line (e.g., 8:00 AM - 10:00 AM)")

    def get_time_list(self):
        return self.time_slots.split('\n')

    def __str__(self):
        return f"{self.title} at {self.branch.branch_name}"

class CoreValue(models.Model):
    COLOR_CHOICES = [
        ('secondary', 'Green (Secondary)'),
        ('accent', 'Gold (Accent)'),
        ('primary', 'Blue (Primary)'),
    ]
    title = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=50, help_text="Enter Lucide icon name")
    description = models.TextField()
    color_scheme = models.CharField(max_length=20, choices=COLOR_CHOICES, default='primary')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title

class Leader(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, related_name='leaders')
    image = models.ImageField(upload_to='leaders/')
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Leadership"

    def __str__(self):
        return f"{self.name} ({self.position})"

class StatementOfFaith(models.Model):
    sof_subtitle = models.CharField(max_length=100, default="Foundations")
    sof_title = models.CharField(max_length=100, default="Statement of Faith")
    sof_description = models.TextField(default="Our beliefs are rooted in...")
    doctrine_pdf = models.FileField(upload_to='doctrines/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Statement of Faith (Header)"

    def __str__(self):
        return "Statement of Faith Header"

class BeliefPoint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
class HistoryMilestone(models.Model):
    year = models.CharField(max_length=4, help_text="Enter the year (e.g., 2012)")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Used to arrange events in order")

    class Meta:
        ordering = ['year', 'order']
        verbose_name_plural = "History Milestones"

    def __str__(self):
        return f"{self.year} - {self.title}"
    
class Statistic(models.Model):
    number = models.CharField(max_length=20, help_text="e.g., 15+ or 500+")
    label = models.CharField(max_length=100, help_text="e.g., Ministries or Members")
    order = models.PositiveIntegerField(default=0, help_text="Order from left to right")

    class Meta:
        ordering = ['order']
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.number} {self.label}"