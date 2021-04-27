from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    identificador = models.CharField(max_length=200)
    albums = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()


class CarSpec(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_brand
