from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings

from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
from imageGeneration.models import Prompt, Image, UserImage


from django.shortcuts import render, get_object_or_404


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

# Addition of imageForge Views

@login_required
def generation(request):
    """Show generation page."""
    return render(request, 'learning_logs/generation.html')

def gallery(request):
    """Show gallery page."""
    return render(request, 'learning_logs/gallery.html')

def user_history(request):
    """Show user history page."""
    return render(request, 'learning_logs/user_history.html')

def about(request):
    """Show the about page."""
    return render(request, 'learning_logs/about.html')

def prompt(request):
    most_recent_prompt = Prompt.objects.latest('date_added')
    context = {'prompt': most_recent_prompt}
    return render(request, 'learning_logs/prompt.html', context)


# Script execution on button click

def run_prompt_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'newPromptInstance.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return redirect('learning_logs:prompt')

def run_image_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'newImageInstance.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return render(request, 'learning_logs/user_image.html')



from django.shortcuts import render, get_object_or_404
from imageGeneration.models import Image, UserImage

def user_image(request):
    # Initialize user_image_instance variable
    user_image_instance = None

    if Image.objects.exists():
        # Get the latest Image object based on the 'datetime_field'
        image_instance_object = Image.objects.latest('datetime_field')

        # Create a new UserImage instance based on the retrieved Image object
        user_image_instance = UserImage.objects.create(
            text_field=image_instance_object.text_field,
            datetime_field=image_instance_object.datetime_field,
            image_field=image_instance_object.image_field,
            local_url=image_instance_object.local_url,
            owner=request.user
        )

        # Pass the field values to the template or do further processing
        context = {
            'text_field': user_image_instance.text_field,
            'datetime_field': user_image_instance.datetime_field,
            'local_url': user_image_instance.local_url,
            'owner': user_image_instance.owner
        }

    else:
        # Handle the case when no Image objects are found
        context = {
            'text_field': None,
            'datetime_field': None,
            'local_url': None,
            'owner': None
        }

    return render(request, 'learning_logs/user_image.html', context)

