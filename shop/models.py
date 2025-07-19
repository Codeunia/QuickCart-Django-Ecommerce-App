from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField()
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField()
    stock=models.CharField()