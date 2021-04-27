from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from music_app.models import Artist
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import CarSpecSerializer
from .models import CarSpec


def homePageView(request):
    return HttpResponse('Hello, World!')


# path: /artists/
def getAllArtist(request):

    if request.method == 'GET':
        requestArtist = Artist.objects.values()
        data = list(requestArtist)
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        print('hola estoy en post')
        print(request)


class CarSpecViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecSerializer

    def get_queryset(self):
        car_spec = CarSpec.objects.all()
        return car_spec

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        cars = CarSpec.objects.filter(id=params['pk'])  # filtrando por id
        serializer = CarSpecSerializer(cars, many=True)
        return Response(serializer.data)
