from rest_framework import serializers
from .models import CarSpec


class CarSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpec
        fields = '__all__'
