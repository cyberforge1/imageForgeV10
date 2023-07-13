import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()


from imageGeneration.models import Image
from saveImage import local_image_path

from django.utils import timezone
from imageGeneration.models import Image

from newPromptInstance import prompt_instance


    # Create a new instance of the Image model
imageModel = Image()

    # Set the values for the fields
imageModel.text_field = prompt_instance
imageModel.datetime_field = timezone.now()
imageModel.image_field = local_image_path
imageModel.local_url = f'http://127.0.0.1:8000/media/{imageModel.image_field}'

    # Save the instance to the database
imageModel.save()

    # Print the field values
print("Text Field:", imageModel.text_field)
print("Datetime Field:", imageModel.datetime_field)
print("Image Field:", imageModel.image_field)
print("Local Image URL Field:", imageModel.local_url)
print("Specific Image Instance ID:", imageModel.id)
    
    
#create_image_instance()


image_model = Image.objects.latest('datetime_field')
image_model_id = image_model.id
print(image_model_id)

