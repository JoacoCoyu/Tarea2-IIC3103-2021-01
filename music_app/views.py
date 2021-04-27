from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from music_app.models import Artist


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
