from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response


def homePageView(request):
    return HttpResponse('Hello, World!')


# class CarSpecViewset(viewsets.ModelViewSet):
#     serializer_class = CarSpecSerializer

#     def get_queryset(self):
#         car_spec = CarSpec.objects.all()
#         return car_spec

#     def retrieve(self, request, *args, **kwargs):
#         # usar %20 para los espacios en las rutas
#         params = kwargs
#         print(params['pk'])
#         params_list = params['pk'].split('-')

#         if len(params_list) == 1:
#             cars = CarSpec.objects.filter(
#                 car_brand=params_list[0])  # filtrando por id
#             serializer = CarSpecSerializer(cars, many=True)
#             return Response(serializer.data)

#         elif len(params_list) == 2:
#             cars = CarSpec.objects.filter(
#                 car_brand=params_list[0], car_model=params_list[1])  # filtrando por id y brand
#             serializer = CarSpecSerializer(cars, many=True)
#             return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         car_data = request.data
#         #print('haciendo post')
#         #return Response(car_data)

#         new_car = CarSpec.objects.create(car_brand=car_data['car_brand'],
#                                          car_model=car_data['car_model'],
#                                          production_year=car_data['production_year'],
#                                          car_body=car_data['car_body'],
#                                          engine_type=car_data['engine_type'])

#         new_car.save()
#         serializer = CarSpecSerializer(new_car)
#         return Response(serializer.data)
