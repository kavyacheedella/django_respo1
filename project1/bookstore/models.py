from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
# Regex in Models (Validation)
class Bookstore(models.Model):
    Bookname = models.CharField(max_length=100 ,
                                validators =
                                [
                                    RegexValidator(
                                        regex=r'^[A-Za-z ]+$',
                                        message = 'Book name must contain only letters and spaces'
                                    )
                                ]
                            )

    Author = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Rating = models.DecimalField(max_digits=2,decimal_places=1)

