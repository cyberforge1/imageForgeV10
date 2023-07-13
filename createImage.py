import openai
from dotenv import load_dotenv
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()
from imageGeneration.models import Prompt
from newPromptInstance import prompt_instance

load_dotenv()
my_variable = os.environ.get('OPENAI_API_KEY')

openai.api_key = os.getenv("OPENAI_API_KEY")


print(prompt_instance)

def generateImageURL():
    
    response = openai.Image.create(
        prompt=prompt_instance,
        n=1,
        size="256x256",
    )
    print(response["data"][0]["url"])
    return response["data"][0]["url"]
