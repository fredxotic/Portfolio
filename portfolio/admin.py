from django.contrib import admin
from .models import (
    Profile, Skill, Education, Certification, Interest,
    Project, ProjectImage, ProjectTag, CareerGoal, ContactMessage
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'profile_image', 'hero_image')
        }),
        ('Contact Details', {
            'fields': ('location', 'phone', 'email')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'instagram_url')
        }),
        ('Documents', {
            'fields': ('cv_file',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'order']
    list_editable = ['percentage', 'order']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'degree_level', 'start_year', 'is_current']
    list_filter = ['degree_level', 'is_current']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'is_current', 'order']
    list_editable = ['order']

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order']
    list_editable = ['order']

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 3

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'project_date', 'order']
    list_filter = ['category', 'featured']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline, ProjectTagInline]
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'short_description', 'thumbnail')
        }),
        ('Content', {
            'fields': ('description', 'detailed_content')
        }),
        ('Project Details', {
            'fields': ('tech_stack', 'project_date', 'live_url', 'github_url')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
    )

@admin.register(CareerGoal)
class CareerGoalAdmin(admin.ModelAdmin):
    list_display = ['timeframe', 'title', 'order']
    list_filter = ['timeframe']
    list_editable = ['order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    list_editable = ['read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']