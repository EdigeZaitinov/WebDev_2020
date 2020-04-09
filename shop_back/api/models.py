from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.TextField()
    count=models.IntegerField()
    category=models.CharField(max_length=30)

class Category(models.Model):
    name=models.CharField(max_length=30)
