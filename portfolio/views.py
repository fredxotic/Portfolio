from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import logging

from .models import (
    Profile, Skill, Education, Certification, Interest,
    Project, CareerGoal
)
from .forms import ContactForm 

# Setup logger
logger = logging.getLogger(__name__)

def home(request):
    # Guard: if no profile exists render a minimal page
    profile = Profile.objects.first()

    # 1. Handle Form Submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            contact_msg = form.save()
            
            # Send Emails (Logic separated for clarity)
            send_notification_emails(contact_msg)
            
            messages.success(request, 'Your message has been sent successfully!')
            
            # Handle AJAX (if used by your frontend JS)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent!'})
            
            return redirect('home')
        else:
            # Form is invalid
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    # 2. Get Data
    skills = Skill.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    interests = Interest.objects.all()
    projects = Project.objects.filter(featured=True).prefetch_related('tags') 
    career_goals = CareerGoal.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'education': education,
        'certifications': certifications,
        'interests': interests,
        'projects': projects,
        'career_goals': career_goals,
        'form': form, 
    }
    
    return render(request, 'index.html', context)

def portfolio_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    profile = Profile.objects.first()
    related_projects = (
        Project.objects
        .exclude(slug=slug)
        .filter(category=project.category)
        .prefetch_related('tags')[:3]
    )
    context = {
        'project': project,
        'profile': profile,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio-details.html', context)

def send_notification_emails(instance):
    """Helper function to handle email sending logic"""
    try:
        # Email to Admin
        send_mail(
            f'Portfolio Contact: {instance.subject}',
            f"From: {instance.name}\nEmail: {instance.email}\n\n{instance.message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        # Email to User
        send_mail(
            f'Thank you for contacting me - {instance.subject}',
            f"Hi {instance.name},\n\nI received your message. I'll get back to you shortly.",
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=True,
        )
    except Exception as e:
        logger.error(f"Email sending failed: {e}")