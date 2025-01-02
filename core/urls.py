from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
] 