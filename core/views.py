from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Project, SkillCategory, Experience, Technology, Contact
from django.http import JsonResponse
import requests
from huggingface_hub import InferenceClient
from django.conf import settings

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Message sent successfully!')
        return redirect('home')

    context = {
        'live_projects': Project.objects.filter(is_live=True).order_by('-created_at')[:3],
    }
    return render(request, 'core/home.html', context)

def about(request):
    about_obj = About.objects.first()
    print("About:", about_obj)  # Debug print
    context = {
        'about': about_obj,
    }
    return render(request, 'core/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all(),
        'technologies': Technology.objects.all(),
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

            # Handle different types of queries
            if any(greeting in message for greeting in ['hi', 'hello', 'hey', 'how are you']):
                return JsonResponse({
                    'response': "Hello! I'm doing well, thank you for asking. I'm here to help you learn about Jaya's portfolio. Would you like to know about his projects, skills, or experience?"
                })
                
            elif 'project' in message:
                return JsonResponse({
                    'response': f"Here are Jaya's notable projects:{projects_context}"
                })
                
            elif 'skill' in message:
                return JsonResponse({
                    'response': f"Here are Jaya's skills by category:{skills_context}"
                })
                
            elif 'experience' in message or 'work' in message:
                experiences = Experience.objects.all().order_by('-start_date')
                exp_text = "\n".join([f"- {exp.position} at {exp.company}" for exp in experiences])
                return JsonResponse({
                    'response': f"Here's Jaya's work experience:\n{exp_text}"
                })
                
            elif 'contact' in message or 'email' in message:
                return JsonResponse({
                    'response': f"You can contact Jaya via email at {about.email if about and about.email else 'the contact form on this website'}. You can also find him on LinkedIn and GitHub through the links in the About section."
                })
                
            else:
                return JsonResponse({
                    'response': "I can tell you about Jaya's projects, skills, work experience, or how to contact him. What would you like to know?"
                })
                
        except Exception as e:
            print(f"Chatbot Error: {str(e)}")
            return JsonResponse({
                'response': "I'm here to help! Would you like to know about Jaya's projects, skills, or experience?"
            })
            
    return JsonResponse({'error': 'Invalid request'}, status=400)
