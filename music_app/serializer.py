from rest_framework import serializers
from .models import CarSpec, Artist, Album


class CarSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpec
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
