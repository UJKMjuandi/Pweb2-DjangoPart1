from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length= 100)
    apellidos = models.CharField(max_length= 100)
    edad = models.IntegerField(max_digits = 3)#(max_d)

INSTALLED_APPS = {
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personas',
}