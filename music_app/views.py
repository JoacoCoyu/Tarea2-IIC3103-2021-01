from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from music_app.models import Artist



def homePageView(request):
    return HttpResponse('Hello, World!')

def getAllArtist(request):

    if request.method == 'GET':

        requestArtist = Artist.objects.values()
        print("estoy en artist")
        data = list(requestArtist)
        return JsonResponse(data, safe=False)
