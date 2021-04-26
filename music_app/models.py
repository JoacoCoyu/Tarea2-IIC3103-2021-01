from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    identificador = models.CharField(max_length=200)
    albums = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()
