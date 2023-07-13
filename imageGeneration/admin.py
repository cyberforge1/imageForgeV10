from django.contrib import admin

from .models import Prompt, Image, UserImage

admin.site.register(Prompt)

admin.site.register(Image)

admin.site.register(UserImage)