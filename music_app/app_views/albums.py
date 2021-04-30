from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


@csrf_exempt
@api_view(["POST", "GET"])
# artists/<str:artist_id>/albums
def artists_albums(request, artist_id):  # artist_id = codificacion del name

    album_artist = models.Artist.objects.filter(identificador=artist_id)
    data_album_artist = list(album_artist.values())

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':  # GET all albums from artist artist_id

        if data_album_artist:
            all_albums = models.Album.objects.filter(
                artist_id_id=data_album_artist[0]['id'])
            data_albums = list(all_albums.values())
            return JsonResponse(data_albums, safe=False, status=200)

        else:
            return JsonResponse({"mesagge": "Albums not found"}, status=404)

    elif request.method == 'POST':  # POST new album from artist artist_id
        valid_inputs = []
        album_data = request.data
        for key in album_data.keys():
            valid_inputs.append(key)

        if valid_inputs != ['name', 'genre']:
            return JsonResponse({"mesagge": "Invalid input"}, safe=False, status=400)

        encoded = b64encode(album_data['name'].encode()).decode('utf-8')
        exists_album = models.Album.objects.filter(identificador=encoded)
        data_album = list(exists_album.values())

        if not data_album:
            new_album = models.Album.objects.create(name=album_data['name'],
                                                    identificador=encoded[0:22],
                                                    genre=album_data['genre'],
                                                    artist_id_id=data_album_artist[0]['id']
                                                    # artist=artists_data['artist'],
                                                    # tracks=artists_data['tracks'],
                                                    # myself=artists_data['myself'],
                                                    )
            new_album.save()
            new_album = models.Album.objects.filter(id=new_album.id)
            data_new_album = list(new_album.values())
            return JsonResponse(data_new_album, safe=False, status=201)

        else:
            return JsonResponse(data_album, safe=False, status=409)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
# albums
def albums(request):

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':  # GET all albums
        data = list(models.Album.objects.values())
        return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
# albums/<str:album_id>
def albums_detail(request, album_id):

    album = models.Album.objects.filter(identificador=album_id)
    data_album = list(album.values())

    if request.method == 'GET':  # GET album with album_id
        if data_album:
            return JsonResponse(data_album, safe=False, status=200)
        else:
            return JsonResponse({"mesagge": "Album not found"}, status=409)

    elif request.method == 'DELETE':  # DELETE artist with artist_id
        if data_album:
            album.delete()
            return JsonResponse({"mesagge": "Album was deleted"}, status=204)
        else:
            return JsonResponse({"mesagge": "Album not found"}, status=404)
