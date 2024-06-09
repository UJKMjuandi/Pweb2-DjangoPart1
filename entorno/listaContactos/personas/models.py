from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.TextField()
    apellidos = models.TextField()
    edad = models.TextField()

INSTALLED_APPS = {
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personas'
}