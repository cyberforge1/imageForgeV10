"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('generation/', views.generation, name='generation'),
    # Page that displays the generated images
    path('gallery/', views.gallery, name='gallery'),
    # Page that displays the user image generation history
    path('user_history/', views.user_history, name='user_history'),
    # Page to show the about us content
    path('about/', views.about, name='about'),
    
    # Page to display the current prompt instance text
    path('prompt/', views.prompt, name='prompt'),
    
    #Addition for button click execution of newPromptInstance
    path('run_prompt_script/', views.run_prompt_script, name='run_prompt_script'),
    
    #Addition for button click execution of newImageInstance
    path('run_image_script/', views.run_image_script, name='run_image_script'),
    
    #Addition for the page to create a request by user
    path('user_image/', views.user_image, name='user_image'),
    
]