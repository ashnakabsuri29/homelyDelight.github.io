from django.db import models
# Create your models here.
from django.contrib.auth.models import User




class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=256)
    number = models.CharField(max_length=10)
    email =  models.CharField(max_length=256)
    role = models.BooleanField(null=True)

class Dish(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    flavour = models.CharField(max_length=256)
    preference = models.CharField(max_length=256)
    veg = models.BooleanField()
    img = models.CharField(max_length=256)
    specialty = models.BooleanField(null=True)
    cook = models.ForeignKey(Cook,on_delete=models.CASCADE,null=True)

class Cart(models.Model):
    cust = models.OneToOneField(Cook,null=True,on_delete=models.PROTECT)
    items = models.ManyToManyField(Dish)


