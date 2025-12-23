from django.db import models

# Create your models here.

class Bookstore(models.Model):
    Bookname = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Rating = models.DecimalField(max_digits=2,decimal_places=1)

