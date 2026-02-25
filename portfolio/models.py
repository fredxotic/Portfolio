from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Fred Kaloki")
    title = models.CharField(max_length=200, default="BCom Student, CPA Candidate, Data Science Enthusiast")
    bio = models.TextField()
    location = models.CharField(max_length=100, default="Nairobi, Kenya")
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # Resizes to 500x500 square for avatar
    profile_image = ProcessedImageField(
        upload_to='profile/',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )
    
    # Resizes to max width 1920 (Full HD) for hero
    hero_image = ProcessedImageField(
        upload_to='hero/',
        processors=[ResizeToFit(1920, 1080)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )
    cv_file = models.FileField(upload_to='docs/', blank=True)
    
    # Social Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name

    def get_typed_titles(self):
        """Return comma-separated title roles for typed.js.
        If title already contains commas it is used as-is.
        Otherwise the full title string is returned for single-item typing.
        """
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)  # blank=True required for form validation
    is_current = models.BooleanField(default=False)
    degree_level = models.CharField(max_length=50, choices=[
        ('High School', 'High School'),
        ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'),
        ('Postgraduate', 'Postgraduate'),
    ])
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_year']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-graph-up-arrow)")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('AI', 'AI & Data Science'),
        ('Web', 'Web Development'),
        ('Mobile', 'Mobile Development'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    detailed_content = models.TextField()
    
    # Project Info
    tech_stack = models.CharField(max_length=200)
    project_date = models.CharField(max_length=50)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    
    # Images
    # Resizes to 800x600 for thumbnail (Standard card size)
    thumbnail = ProcessedImageField(
        upload_to='projects/',
        processors=[ResizeToFill(800, 600)],
        format='JPEG',
        options={'quality': 85},
        blank=True, 
        null=True
    )

    # Display
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    # Gallery images
    image = ProcessedImageField(
        upload_to='projects/gallery/',
        processors=[ResizeToFit(1200, 800)],
        format='JPEG',
        options={'quality': 85}
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — Image {self.order}"

class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class CareerGoal(models.Model):
    TIMEFRAME_CHOICES = [
        ('short', '1-2 Years'),
        ('medium', '3-4 Years'),
        ('long', '5+ Years'),
    ]
    
    timeframe = models.CharField(max_length=10, choices=TIMEFRAME_CHOICES)
    title = models.CharField(max_length=100)
    goals = models.TextField(help_text="Enter each goal on a new line")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.get_timeframe_display()} - {self.title}"
    
    def get_goals_list(self):
        return [goal.strip() for goal in self.goals.split('\n') if goal.strip()]

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"