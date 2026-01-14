from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',
                message="Invalid email format"
            )
        ]
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(99)
        ]
    )
    city = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
