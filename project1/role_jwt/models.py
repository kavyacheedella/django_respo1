from django.db import models

# Create your models here.
class RoleDetails(models.Model):
    username = models.CharField(max_length=20 , unique = True) 
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10 , default="user")
