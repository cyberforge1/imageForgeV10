from django.shortcuts import render
from .models import Prompt, Image, UserImage
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def image(request):
    '''Show all images'''
    image = UserImage.objects.filter(owner=request.user).order_by('datetime_field')

    image = list(reversed(image))
    context = {
        'image': image,
    }
    return render(request, 'imageGeneration/image.html', context)


def gallery(request):
    '''Show the gallery'''
    gallery = Image.objects.all().order_by('datetime_field')
    gallery = list(reversed(gallery))
    context = {
        'gallery': gallery,
    }
    return render(request, 'imageGeneration/gallery.html', context)

def prompt(request):
    '''Get the most recent prompt instance'''
    most_recent_prompt = Prompt.objects.latest('date_added')
    context = {'prompt': most_recent_prompt}
    return render(request, 'imageGeneration/prompt.html', context)