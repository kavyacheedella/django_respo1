from django.db import models

# Create your models here.
class userProfile(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()

class employeeProfile(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_email = models.EmailField(unique=True)

    

