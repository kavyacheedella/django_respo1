from django.db import models
import uuid
# Create your models here.

class OrderDetails(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField(unique=True)
    orderid = models.CharField(max_length=50,unique=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    paymentmode = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    dateandtime = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(default="INR",max_length=50)
    transcationid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)



#uuid1 -- generates a random num based on time and mac
#uuid4 -- generates a random num by combination of digits and characters 
#uuid5 -- generates a random num by combination of username and spl characters