from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


def foo(a):
    for b in a:
        yield b


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def artists_albums(request, artist_id):  # artist_id = codificacion del name

    album_artist = models.Artist.objects.filter(identificador=artist_id)
    data_album_artist = list(album_artist.values())
    print(artist_id)

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        all_albums = models.Album.objects.filter(
            artist_id_id=data_album_artist[0]['id'])
        data_albums = list(all_albums.values())
        return JsonResponse(data_albums, safe=False)

    elif request.method == 'POST':
        album_data = request.data
        encoded = b64encode(album_data['name'].encode()).decode('utf-8')
        new_album = models.Album.objects.create(name=album_data['name'],
                                                identificador=encoded,
                                                genre=album_data['genre'],
                                                artist_id_id=data_album_artist[0]['id']
                                                # artist=artists_data['artist'],
                                                # tracks=artists_data['tracks'],
                                                # myself=artists_data['myself'],
                                                )
        new_album.save()
        new_album = models.Album.objects.filter(id=new_album.id)
        data_new_album = list(new_album.values())
        return JsonResponse(data_new_album, safe=False)
        # return JsonResponse({"msg": "ruta delete en construccion"}, safe=False)
