from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prompt(models.Model):
    '''A prompt generated for the user'''
    prompt_id = models.AutoField(primary_key=True)  # Add the ID field
    text_field = models.TextField()  # Rename the field to avoid conflicts
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.date_added
    
    def get_id(self):
        return self.prompt_id
    
    
    
class Image(models.Model):
    text_field = models.TextField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    image_field = models.ImageField(upload_to='images/')
    local_url = models.TextField()

    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.datetime_field

    def get_image_url(self):
        if self.image_field:
            return self.image_field.url
        return None
    
    def get_local_url(self):
        return self.local_url
    
    
class UserImage(models.Model):
    text_field = models.TextField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    image_field = models.ImageField(upload_to='images/')
    local_url = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_text(self):
        return self.text_field

    def get_datetime(self):
        return self.datetime_field

    def get_image_url(self):
        if self.image_field:
            return self.image_field.url
        return None
    
    def get_local_url(self):
        return self.local_url
    
    def get_owner(self):
        return self.owner
