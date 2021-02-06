from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    languages = models.TextField()
    technology = models.TextField()
    image = models.FilePathField(path="/img")
