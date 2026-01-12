from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,related_name='sign_up_profile')
    has_hall_ticket = models.BooleanField(default=False)
    attendance_percentage = models.IntegerField(default=0)
    exam_fee_paid = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username