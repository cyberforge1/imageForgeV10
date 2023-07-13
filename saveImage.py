
import os
import requests
import random
from createImage import generateImageURL
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


def generate_random_tag():
    tag = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
    return tag

random_tag = generate_random_tag()
image_path = os.path.join(MEDIA_ROOT, f"image_{random_tag}.jpg")
local_image_path = f"image_{random_tag}.jpg"
    
def save_image_from_url(url):
    response = requests.get(url)
    
    with open(image_path, "wb") as f:
        f.write(response.content)
    
    print(f"Image saved as {image_path}")
    print(image_path)

# Main execution
image_url = generateImageURL()
if image_url:
    save_image_from_url(image_url)




