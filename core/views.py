from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Project, SkillCategory, Experience, Technology, Contact
from django.http import JsonResponse
import requests
from huggingface_hub import InferenceClient
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

def home(request):
    try:
        projects = Project.objects.filter(is_live=True).order_by('-created_at')[:3]
        # Convert image URLs to absolute URLs if they exist
        for project in projects:
            if project.image:
                project.image.url = request.build_absolute_uri(project.image.url)
        context = {'live_projects': projects}
        return render(request, 'core/home.html', context)
    except Exception as e:
        logger.error(f"Error in home view: {str(e)}")
        return render(request, 'core/home.html', {'live_projects': []})

def about(request):
    try:
        about_obj = About.objects.first()
        context = {'about': about_obj}
    except Exception:
        context = {'about': None}
    return render(request, 'core/about.html', context)

def projects(request):
    try:
        projects = Project.objects.all()
        technologies = Technology.objects.all()
        context = {
            'projects': projects,
            'technologies': technologies,
        }
    except Exception as e:
        logger.error(f"Error in projects view: {str(e)}")
        context = {
            'projects': [],
            'technologies': [],
            'error_message': 'Unable to load projects at this time.'
        }
    return render(request, 'core/projects.html', context)

def skills(request):
    context = {
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all()
    }
    return render(request, 'core/skills.html', context)

def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')
    context = {
        'experiences': experiences
    }
    return render(request, 'core/experience.html', context)

def chatbot_response(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        message = message.lower()
        
        try:
            # Get data from database
            skill_categories = SkillCategory.objects.prefetch_related('skills').all()
            projects = Project.objects.prefetch_related('technologies').all()
            about = About.objects.first()
            
            # Format skills context
            skills_context = ""
            for category in skill_categories:
                skills_context += f"\n{category.name}: "
                skills_context += ", ".join([skill.name for skill in category.skills.all()])
            
            # Format projects context
            projects_context = ""
            for project in projects:
                techs = ", ".join([tech.name for tech in project.technologies.all()])
                projects_context += f"\n- {project.title}: {project.description} (Technologies: {techs})"

            if 'project' in message:
                return JsonResponse({
                    'response': f"Here are some of my projects:{projects_context}"
                })
            
            # Add other response conditions here
            return JsonResponse({
                'response': "I can tell you about my projects, skills, work experience, or how to contact me. What would you like to know?"
            })
                
        except Exception as e:
            logger.error(f"Chatbot Error: {str(e)}")
            return JsonResponse({
                'error': True,
                'response': "Sorry, I encountered an error. Please try again."
            })
    
    return JsonResponse({'error': True, 'response': 'Invalid request method'}, status=400)
