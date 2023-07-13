import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()
from createPrompt import generatePrompt
from imageGeneration.models import Prompt

prompt = generatePrompt()

prompt_model = Prompt()
prompt_model.text_field = prompt
prompt_model.save()

prompt_id = prompt_model.prompt_id


# Created to fetch the image prompt text that is displayed on the webpage
last_prompt_id = prompt_id - 1

prompt_instance = Prompt.objects.get(prompt_id=last_prompt_id).text_field

