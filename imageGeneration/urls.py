'''Defines URL patterns for imageGeneration.'''

from django.urls import path

from . import views

app_name = 'imageGeneration'

urlpatterns = [
    # Generated Images
    path('image/', views.image, name='image'),
    # Entire gallery
    path('gallery/', views.gallery, name='gallery'),
    # Prompt
    path('prompt/', views.prompt, name='prompt'),
]