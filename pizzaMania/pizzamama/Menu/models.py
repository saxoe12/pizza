from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=10, default=0.0) 
    ingredient = models.CharField(max_length=100)
    vegetarienne = models.BooleanField(default=False)

def __str__(self):
        return self.name

    