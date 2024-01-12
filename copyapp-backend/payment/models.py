from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerPayment(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    subscriptionid = models.CharField(max_length=255, unique=True)
    customerid = models.CharField(max_length=255, unique=True)
    productid = models.CharField(max_length=255, unique=True)
    priceid = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.customer.email