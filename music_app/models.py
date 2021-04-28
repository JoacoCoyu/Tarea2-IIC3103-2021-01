from django.db import models


class CarSpec(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_brand


class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    identificador = models.CharField(max_length=200)
    albums = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()

    def __str__(self):
        return self.name


class Album(models.Model):
    artist_id = models.ForeignKey(
        Artist, related_name='artist', default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    identificador = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    artist = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()

    def __str__(self):
        return self.name
