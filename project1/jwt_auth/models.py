from django.db import models

# Create your models here.

class details(models.Model):
    username = models.CharField(max_length=20 , unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    
