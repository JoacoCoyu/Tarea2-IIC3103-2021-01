from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def artists_tracks(request, artist_id):

    album_artist = models.Artist.objects.filter(identificador=artist_id)
    data_album_artist = list(album_artist.values())

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        all_albums = models.Album.objects.filter(
            artist_id_id=data_album_artist[0]['id'])
        data_albums = list(all_albums.values())

        all_tracks = []
        for album in data_albums:
            track = models.Track.objects.filter(
                album_id_id=album['id'])
            data_tracks = list(track.values())
            for specific_album in data_tracks:
                all_tracks.append(specific_album)

        return JsonResponse(all_tracks, safe=False)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def albums_tracks(request, album_id):

    track_album = models.Album.objects.filter(identificador=album_id)
    data_track_album = list(track_album.values())

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        all_tracks = models.Track.objects.filter(
            album_id_id=data_track_album[0]['id'])
        data_tracks = list(all_tracks.values())
        return JsonResponse(data_tracks, safe=False)

    elif request.method == 'POST':
        track_data = request.data
        encoded = b64encode(track_data['name'].encode()).decode('utf-8')
        new_track = models.Track.objects.create(name=track_data['name'],
                                                identificador=encoded[0:22],
                                                duration=track_data['duration'],
                                                album_id_id=data_track_album[0]['id']
                                                # artist=artists_data['artist'],
                                                # tracks=artists_data['tracks'],
                                                # myself=artists_data['myself'],
                                                )
        new_track.save()
        new_track = models.Track.objects.filter(id=new_track.id)
        data_new_track = list(new_track.values())
        return JsonResponse(data_new_track, safe=False)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def tracks(request):

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        data = list(models.Track.objects.values())
        return JsonResponse(data, safe=False)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def tracks_detail(request, track_id):

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    elif request.method == 'GET':
        track = models.Track.objects.filter(identificador=track_id)
        data_track = list(track.values())
        return JsonResponse(data_track, safe=False)
