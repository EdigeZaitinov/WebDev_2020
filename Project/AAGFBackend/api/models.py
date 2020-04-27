from django.db import models

class GamesCategory(models.Model):
    category=models.CharField(max_length=30)

class Games(models.Model):
    link=models.TextField()
    name=models.CharField(max_length=50)
    description=models.TextField()
    video=models.TextField()
    category=models.ForeignKey(GamesCategory,on_delete=models.CASCADE)

class FilmsCategory(models.Model):
    category=models.CharField(max_length=30)

class Films(models.Model):
    link=models.TextField()
    name=models.CharField(max_length=50)
    description=models.TextField()
    video=models.TextField()
    category=models.ForeignKey(FilmsCategory,on_delete=models.CASCADE)

class AAGFUsers(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)



