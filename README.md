# Django Web Application - imageForgeV11

ChatGPT & DALL•E 2 Image Generation

This is a Django web application that allows users to generate a random string using ChatGPT-generated data as a unique prompt. Upon clicking a button, the application sends this prompt to the OPENAI DALL•E 2 API to generate a unique image. The generated images are saved in a public gallery and also under the user's account history. The web application has been deployed to Heroku, and the images are stored in an S3 AWS bucket.

## How to Use the Web Application

1. Visit the deployed web application URL on Heroku.
2. Click on the "Generate Random Image" button.
3. The web application will generate a unique string prompt using ChatGPT-generated data.
4. The generated prompt is sent to the OPENAI DALL•E 2 API to create a unique image based on the prompt.
5. The unique image is displayed on the webpage.
6. The generated image is saved in the public gallery accessible to all users.
7. Additionally, the image is saved in the user's account history.

## Important Code Components

Below are the integral code components used to achieve the functionality described above.

### `generatePrompt()` function:

This function randomly generates a string prompt using ChatGPT-generated data based on different classes and data sets.

### `generateImageURL()` function:

This function sends the generated prompt to the OPENAI DALL•E 2 API to generate a unique image based on the prompt. It retrieves the image URL from the API response.

### Saving Images to Local and S3:

The application saves the generated images locally and then uploads them to the S3 AWS bucket for long-term storage and accessibility.

## Installation and Dependencies

The application requires the following dependencies:

```
aiohttp==3.8.4
aiosignal==1.3.1
asgiref==3.7.2
async-timeout==4.0.2
attrs==23.1.0
beautifulsoup4==4.11.1
boto3==1.28.3
botocore==1.31.3
certifi==2023.5.7
charset-normalizer==3.2.0
dj-database-url==2.0.0
Django==4.2.3
django-bootstrap5==21.3
django-heroku==0.3.1
django-storages==1.13.2
frozenlist==1.4.0
gunicorn==20.1.0
idna==3.4
jmespath==1.0.1
multidict==6.0.4
openai==0.27.8
Pillow==10.0.0
psycopg2==2.9.6
python-dateutil==2.8.2
python-dotenv==1.0.0
requests==2.31.0
s3transfer==0.6.1
six==1.16.0
soupsieve==2.3.2.post1
sqlparse==0.4.2
tqdm==4.65.0
typing_extensions==4.7.1
urllib3==1.26.16
whitenoise==6.5.0
yarl==1.9.2
```

## Deployment

The application has been deployed to Heroku and utilizes an S3 AWS bucket to store the images. The necessary configurations and environment variables have been set up for the deployment.

---
