from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


@csrf_exempt
@api_view(["GET", "POST"])
def artists(request):
    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        data = list(models.Artist.objects.values())
        print(data)
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        artist_data = request.data
        encoded = b64encode(artist_data['name'].encode()).decode('utf-8')
        # print(request.data['name'])
        new_artist = models.Artist.objects.create(name=artist_data['name'],
                                                  identificador=encoded[0:22],
                                                  age=artist_data['age']
                                                  #   albums=artists_data['albums'],
                                                  #   tracks=artists_data['tracks'],
                                                  #   myself=artists_data['myself'],
                                                  )
        new_artist.save()
        new_artist = models.Artist.objects.filter(id=new_artist.id)
        data_new_artist = list(new_artist.values())
        return JsonResponse(data_new_artist, safe=False)


# @csrf_exempt
@api_view(["GET", "DELETE"])
def artists_detail(request, artist_id):

    # if request.method not in ('GET', 'POST'):
    #     return HttpResponse(status=405)

    if request.method == 'GET':
        artist = models.Artist.objects.filter(identificador=artist_id)
        data_artist = list(artist.values())
        return JsonResponse(data_artist, safe=False)

    elif request.method == 'DELETE':
        artist = models.Artist.objects.filter(identificador=artist_id)
        artist.delete()
        return JsonResponse({"mesagge": "Artist was deleted"})
