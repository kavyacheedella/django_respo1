from django.db import models
import uuid
# Create your models here.
class MovieBooking(models.Model):
    moviename = models.CharField(max_length=100)
    showtime = models.CharField(max_length=100)
    screenname = models.CharField(max_length=100,default = "screen-1")
    dateandtime = models.DateTimeField(auto_now_add=True)
    transcationid = models.UUIDField(default = uuid.uuid4,unique=True,editable=False)


