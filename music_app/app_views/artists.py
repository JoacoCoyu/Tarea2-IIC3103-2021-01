from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def artists(request):
    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        data = list(models.Artist.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        artist_data = request.data
        encoded = b64encode(artist_data['name'].encode()).decode('utf-8')
        # print(request.data['name'])
        new_artist = models.Artist.objects.create(name=artist_data['name'],
                                                  identificador=encoded,
                                                  age=artist_data['age']
                                                  #   albums=artists_data['albums'],
                                                  #   tracks=artists_data['tracks'],
                                                  #   myself=artists_data['myself'],
                                                  )
        new_artist.save()
        new_artist = models.Artist.objects.filter(id=new_artist.id)
        data_new_artist = list(new_artist.values())
        return JsonResponse(data_new_artist, safe=False)

    elif request.method == 'DELETE':
        print(request.method)
        return JsonResponse({"msg": "ruta delete en construccion"})

        #     def destroy(self, request, *args, **kwargs):
        #         params = kwargs['pk']
        #         params_list = params.split("-")
        #         artist = models.Artist.objects.filter(id=params_list[0])
        #         artist.delete()

        #         return Response({"mesagge": "Artist was deleted"})


@api_view(["POST", "GET", "DELETE"])
def artists_detail(request, artist_id):

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    elif request.method == 'GET':
        artist = models.Artist.objects.filter(id=artist_id)
        data_artist = list(artist.values())
        return JsonResponse(data_artist, safe=False)
