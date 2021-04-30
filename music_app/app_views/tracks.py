from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from base64 import b64encode
from .. import models


api_url = 'https://t2-iic3103-jacouyoumdjian.herokuapp.com/'


@api_view(["GET"])
# artists/<str:artist_id>/tracks
def artists_tracks(request, artist_id):

    album_artist = models.Artist.objects.filter(identificador=artist_id)
    data_album_artist = list(album_artist.values())

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        if data_album_artist:
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

            return JsonResponse(all_tracks, safe=False, status=200)

        else:
            return JsonResponse({"mesagge": "Tracks not found"}, status=404)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
# albums/<str:album_id>/tracks
def albums_tracks(request, album_id):

    track_album = models.Album.objects.filter(identificador=album_id)
    data_track_album = list(track_album.values())

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':  # GET all tracks from album album_id

        if data_track_album:
            all_tracks = models.Track.objects.filter(
                album_id_id=data_track_album[0]['id'])
            data_tracks = list(all_tracks.values())
            return JsonResponse(data_tracks, safe=False, status=200)

        else:
            return JsonResponse({"mesagge": "Tracks not found"}, status=404)

    elif request.method == 'POST':  # POST track from album album_id
        valid_inputs = []
        track_data = request.data
        for key in track_data.keys():
            valid_inputs.append(key)

        if valid_inputs != ['name', 'duration']:
            return JsonResponse({"mesagge": "Invalid input"}, safe=False, status=400)

        encoded = b64encode(track_data['name'].encode()).decode('utf-8')
        exists_track = models.Track.objects.filter(identificador=encoded)
        data_track = list(exists_track.values())

        album_track = models.Album.objects.filter(identificador=album_id)
        data_album_track = list(album_track.values())

        tracks_artist = models.Artist.objects.filter(
            id=data_album_track[0]['artist_id_id'])
        data_tracks_artist = list(tracks_artist.values())
        artist_id = data_tracks_artist[0]['identificador']

        if not data_track:
            new_track = models.Track.objects.create(name=track_data['name'],
                                                    identificador=encoded[0:22],
                                                    duration=track_data['duration'],
                                                    album_id_id=data_track_album[0]['id'],
                                                    artist=api_url +
                                                    f'artists/{artist_id}',
                                                    album=api_url +
                                                    f'albums/{album_id}',
                                                    myself=api_url +
                                                    f'tracks/{encoded[0:22]}',
                                                    )
            new_track.save()
            new_track = models.Track.objects.filter(id=new_track.id)
            data_new_track = list(new_track.values())
            return JsonResponse(data_new_track, safe=False, status=201)

        else:
            return JsonResponse(data_track, safe=False, status=409)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def tracks(request):

    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=405)

    if request.method == 'GET':
        data = list(models.Track.objects.values())
        return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@api_view(["POST", "GET", "DELETE"])
def tracks_detail(request, track_id):

    track = models.Track.objects.filter(identificador=track_id)
    data_track = list(track.values())

    if request.method == 'GET':  # GET album with album_id
        if data_track:
            return JsonResponse(data_track, safe=False, status=200)
        else:
            return JsonResponse({"mesagge": "Track not found"}, status=409)

    elif request.method == 'DELETE':  # DELETE artist with artist_id
        if data_track:
            album.delete()
            return JsonResponse({"mesagge": "Track was deleted"}, status=204)
        else:
            return JsonResponse({"mesagge": "Track not found"}, status=404)


@api_view(["PUT"])
# tracks/<str:track_id>/play
def play_tracks(request, track_id):
    track = models.Track.objects.filter(identificador=track_id)
    data_track = list(track.values())

    if request.method == 'PUT':
        if data_track:
            updated_plays = track.values()[0]['times_played'] + 1
            track.values().update(times_played=updated_plays)

            return JsonResponse({"mesagge": "Track played"}, status=200)

        else:
            return JsonResponse({"mesagge": "Track not found"}, status=404)


@csrf_exempt
@api_view(["PUT"])
# albums/<str:album_id>/tracks/play
def play_album_tracks(request, album_id):
    track_album = models.Album.objects.filter(identificador=album_id)
    data_track_album = list(track_album.values())

    if request.method == 'PUT':
        if data_track_album:
            all_tracks = models.Track.objects.filter(
                album_id_id=data_track_album[0]['id'])
            for i_track in range(len(list(all_tracks.values()))):
                track_identificador = all_tracks.values()[
                    i_track]['identificador']
                update_track = models.Track.objects.filter(
                    identificador=track_identificador)
                updated_plays = update_track.values()[0]['times_played'] + 1
                update_track.values().update(times_played=updated_plays)

            return JsonResponse({"mesagge": "Album tracks played"}, status=200)

        else:
            return JsonResponse({"mesagge": "Album not found"}, status=404)


@csrf_exempt
@api_view(["PUT"])
# artists/<str:artist_id>/albums/play
def play_artist_tracks(request, artist_id):
    album_artist = models.Artist.objects.filter(identificador=artist_id)
    data_album_artist = list(album_artist.values())

    if request.method == 'PUT':
        if data_album_artist:
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

            for i_track in range(len(all_tracks)):
                track_identificador = all_tracks[i_track]['identificador']
                update_track = models.Track.objects.filter(
                    identificador=track_identificador)
                updated_plays = update_track.values()[0]['times_played'] + 1
                update_track.values().update(times_played=updated_plays)

            return JsonResponse({"mesagge": "artist tracks played"}, status=200)

        else:
            return JsonResponse({"mesagge": "Artist not found"}, status=404)