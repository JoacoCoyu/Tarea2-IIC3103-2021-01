from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


api_url = 'https://t2-iic3103-jacouyoumdjian.herokuapp.com/'


@api_view(["GET", "POST"])  # artists
def artists(request):
    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':  # GET all artists
        data_artists = list(models.Artist.objects.values())
        for artist in data_artists:
            artist["self"] = artist["myself"]
            del artist["myself"]
            del artist["id"]
            del artist["identificador"]
        print(data_artists)
        return JsonResponse(data_artists, safe=False, status=200)

    elif request.method == 'POST':  # POST a new artist
        valid_inputs = []
        artist_data = request.data
        for key in artist_data.keys():
            valid_inputs.append(key)

        if valid_inputs != ['name', 'age']:
            return JsonResponse({"mesagge": "Invalid input"}, status=400)

        else:
            request_name = request.data["name"]
            request_age = request.data["age"]
            if (type(request_name) != str) or (type(request_age) != int):
                return JsonResponse({"mesagge": "Invalid input"}, status=400)

        encoded = b64encode(artist_data['name'].encode()).decode('utf-8')
        exists_artist = models.Artist.objects.filter(identificador=encoded)
        data_artist = list(exists_artist.values())

        if not data_artist:
            new_artist = models.Artist.objects.create(name=artist_data['name'],
                                                      identificador=encoded[0:22],
                                                      age=artist_data['age'],
                                                      albums=api_url +
                                                      f'artists/{encoded[0:22]}/albums',
                                                      tracks=api_url +
                                                      f'artists/{encoded[0:22]}/tracks',
                                                      myself=api_url +
                                                      f'artists/{encoded[0:22]}'
                                                      )
            new_artist.save()
            new_artist = models.Artist.objects.filter(id=new_artist.id)
            data_new_artist = list(new_artist.values())
            data_new_artist[0]["self"] = data_new_artist[0]["myself"]
            del data_new_artist[0]["myself"]
            del data_new_artist[0]["id"]
            del data_new_artist[0]["identificador"]
            return JsonResponse(data_new_artist, safe=False, status=201)

        else:
            data_artist[0]["self"] = data_artist[0]["myself"]
            del data_artist[0]["myself"]
            del data_artist[0]["id"]
            del data_artist[0]["identificador"]
            return JsonResponse(data_artist, safe=False, status=409)


@api_view(["GET", "DELETE"])  # artists/<str:artist_id>
def artists_detail(request, artist_id):

    artist = models.Artist.objects.filter(identificador=artist_id)
    data_artist = list(artist.values())

    if request.method == 'GET':  # GET artist with artist_id
        if data_artist:
            data_artist[0]["self"] = data_artist[0]["myself"]
            del data_artist[0]["myself"]
            del data_artist[0]["id"]
            del data_artist[0]["identificador"]
            return JsonResponse(data_artist, safe=False, status=200)
        else:
            return JsonResponse({"mesagge": "Artist not found"}, status=404)

    elif request.method == 'DELETE':  # DELETE artist with artist_id
        if data_artist:
            artist.delete()
            return JsonResponse({"mesagge": "artista eliminado"}, status=204)
        else:
            return JsonResponse({"mesagge": "artista inexistente"}, status=404)
