from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class AboutSection(models.Model):
    # Header Section
    title = models.CharField(max_length=200, default="Our Story & Vision")
    subtitle = models.CharField(max_length=100, default="Who We Are")
    main_image = models.ImageField(upload_to='about/', null=True, blank=True)
    established_year = models.CharField(max_length=20, default="Est. 2012")
    established_text = models.CharField(max_length=100, default="A Decade of Grace")
    foundation_quote = models.TextField(default="A garden where souls are nurtured by grace and set on fire by the Spirit.", help_text="A short summary or mandate of your founding.")
    description = CKEditor5Field('Content', config_name='default', default="")
    
    # Mission Section
    mission_subtitle = models.CharField(max_length=100, default="Our Purpose")
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_description = CKEditor5Field('Content', config_name='default', default="To cultivate a global garden...")

    vision_title = models.CharField(max_length=100, default="Our Vision")
    vision_description = CKEditor5Field('Content', config_name='default', default="To see the fragrance of God's presence...")

    # Statement of Faith Section (Integrated)
    sof_subtitle = models.CharField(max_length=100, default="Foundations")
    sof_title = models.CharField(max_length=100, default="Statement of Faith")
    sof_description = CKEditor5Field('Content', config_name='default', default="Our beliefs are rooted in...")
    doctrine_pdf = models.FileField(upload_to='doctrines/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "About Section (Main)"

    def __str__(self):
        return "Main About Page Content"

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
    description = CKEditor5Field('Content', config_name='default')
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
    contact_email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Leadership"

    def __str__(self):
        return f"{self.name} ({self.position})"


class BeliefPoint(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='beliefs', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Belief Points (Cards)"

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
# Founding Pastor Page Model
class FoundingPastor(models.Model):
    # Section 1: Hero
    hero_title = models.CharField(max_length=200, default="Our Founding Pastor")
    hero_subtitle = models.CharField(max_length=200, default="The Visionary Behind TVA")
    hero_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 2: Biography
    bio_title = models.CharField(max_length=200, default="His Story")
    bio_content = CKEditor5Field('Content', config_name='default', default="")
    bio_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 3: Vision
    vision_title = models.CharField(max_length=200, default="Founding Vision")
    vision_content = CKEditor5Field('Content', config_name='default', default="")
    vision_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 4: Legacy
    legacy_title = models.CharField(max_length=200, default="His Legacy")
    legacy_content = CKEditor5Field('Content', config_name='default', default="")
    legacy_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 5: Quotes
    quotes_title = models.CharField(max_length=200, default="Words of Wisdom")
    featured_quote = models.TextField(default="")
    quote_author = models.CharField(max_length=100, default="Founding Pastor")
    quote_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 6: Timeline
    timeline_title = models.CharField(max_length=200, default="Ministry Timeline")
    timeline_image = models.ImageField(upload_to='pastors/', null=True, blank=True)

    # Section 7: Contact & Social
    contact_title = models.CharField(max_length=200, default="Connect With Founding Pastor")
    contact_email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    mixlr_url = models.URLField(blank=True, null=True)
    threads_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True, verbose_name="X (Twitter) URL")
    tiktok_url = models.URLField(blank=True, null=True)
    medium_url = models.URLField(blank=True, null=True, help_text="Link to Medium articles")

    # Section 8: Books
    books_title = models.CharField(max_length=200, default="Books & Resources")
    selar_book_url = models.URLField(blank=True, null=True, help_text="Link to Selar store/book")
    amazon_book_url = models.URLField(blank=True, null=True, help_text="Link to Amazon author page/book")
    
    class Meta:
        verbose_name_plural = "Founding Pastor Page"
    
    def __str__(self):
        return "Founding Pastor Page Content"

# Presiding Pastor Page Model
class PresidingPastor(models.Model):
    # Section 1: Hero
    hero_title = models.CharField(max_length=200, default="Our Presiding Pastor")
    hero_subtitle = models.CharField(max_length=200, default="Leading TVA Today")
    hero_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    pastor_name = models.CharField(max_length=200, default="Pastor Name")
    
    # Section 2: Biography
    bio_title = models.CharField(max_length=200, default="Meet Our Pastor")
    bio_content = CKEditor5Field('Content', config_name='default', default="")
    bio_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 3: Vision
    vision_title = models.CharField(max_length=200, default="Vision for TVA")
    vision_content = CKEditor5Field('Content', config_name='default', default="")
    vision_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 4: Ministry Focus
    focus_title = models.CharField(max_length=200, default="Ministry Focus")
    focus_content = CKEditor5Field('Content', config_name='default', default="")
    focus_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 5: Message
    message_title = models.CharField(max_length=200, default="A Word From Pastor")
    message_content = CKEditor5Field('Content', config_name='default', default="")
    message_image = models.ImageField(upload_to='pastors/', null=True, blank=True)
    
    # Section 6: Contact
    contact_title = models.CharField(max_length=200, default="Connect With Pastor")
    contact_email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    mixlr_url = models.URLField(blank=True, null=True)
    threads_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True, verbose_name="X (Twitter) URL")
    tiktok_url = models.URLField(blank=True, null=True)
    medium_url = models.URLField(blank=True, null=True, help_text="Link to Medium articles")

    # Section 7: Books
    books_title = models.CharField(max_length=200, default="Books & Resources")
    selar_book_url = models.URLField(blank=True, null=True, help_text="Link to Selar store/book")
    amazon_book_url = models.URLField(blank=True, null=True, help_text="Link to Amazon author page/book")
    
    class Meta:
        verbose_name_plural = "Presiding Pastor Page"
    
    def __str__(self):
        return "Presiding Pastor Page Content"

# Pastoral Team Page Model
class PastoralTeam(models.Model):
    # Section 1: Hero
    hero_title = models.CharField(max_length=200, default="Our Pastoral Team")
    hero_subtitle = models.CharField(max_length=200, default="Serving Together in Unity")
    hero_image = models.ImageField(upload_to='pastoral_team/', null=True, blank=True)
    
    # Section 2: Overview
    overview_title = models.CharField(max_length=200, default="Meet The Team")
    overview_content = CKEditor5Field('Content', config_name='default', default="")
    overview_image = models.ImageField(upload_to='pastoral_team/', null=True, blank=True)
    
    # Section 3: Team Structure
    structure_title = models.CharField(max_length=200, default="Our Structure")
    structure_content = CKEditor5Field('Content', config_name='default', default="")
    structure_image = models.ImageField(upload_to='pastoral_team/', null=True, blank=True)
    
    # Section 4: Team Values
    values_title = models.CharField(max_length=200, default="Our Values")
    values_content = CKEditor5Field('Content', config_name='default', default="")
    values_image = models.ImageField(upload_to='pastoral_team/', null=True, blank=True)
    
    # Section 5: Ministry Areas (handled by team members below)
    ministry_title = models.CharField(max_length=200, default="Ministry Areas")
    
    # Section 6: Join Team
    join_title = models.CharField(max_length=200, default="Join Our Team")
    join_content = CKEditor5Field('Content', config_name='default', default="")
    join_image = models.ImageField(upload_to='pastoral_team/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Pastoral Team Page"
    
    def __str__(self):
        return "Pastoral Team Page Content"

# Timeline Milestone for Founding Pastor
class PastoralTimeline(models.Model):
    founding_pastor = models.ForeignKey(FoundingPastor, on_delete=models.CASCADE, related_name='timeline_events', null=True, blank=True)
    year = models.CharField(max_length=4, help_text="e.g., 2012")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['year', 'order']
        verbose_name_plural = "Pastoral Timeline Events"
    
    def __str__(self):
        return f"{self.year} - {self.title}"

# Team Member for Pastoral Team
class TeamMember(models.Model):
    pastoral_team = models.ForeignKey(PastoralTeam, on_delete=models.CASCADE, related_name='team_members', null=True, blank=True)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='team_members/', null=True, blank=True)
    ministry_area = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Team Members"
    
    def __str__(self):
        return f"{self.name} - {self.position}"
