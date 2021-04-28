from rest_framework import viewsets
from rest_framework.response import Response
from base64 import b64encode
from .. import serializer
from .. import models


class AlbumViewset(viewsets.ModelViewSet):

    serializer_class = serializer.AlbumSerializer

    def get_queryset(self):

        album_data = models.Album.objects.all()
        return album_data

    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('-')

        # if len(params_list) == 1:
        album = models.Album.objects.filter(
            id=params_list[0])  # filtrando por id
        data_serialize = serializer.AlbumSerializer(album, many=True)
        return Response(data_serialize.data)

    def create(self, request, *args, **kwargs):
        album_data = request.data
        encoded = b64encode(album_data['name'].encode()).decode('utf-8')

        new_album = models.Album.objects.create(name=album_data['name'],
                                                identificador=encoded,
                                                genre=album_data['genre'],
                                                artist=album_data['artist'],
                                                tracks=album_data['tracks'],
                                                myself=album_data['myself'],
                                                artist_id=models.Artist.objects.get(id=album_data['artist_id']))

        new_album.save()
        data_serialize = serializer.AlbumSerializer(new_album)
        return Response(data_serialize.data)

    def destroy(self, request, *args, **kwargs):
        params = kwargs['pk']
        params_list = params.split("-")
        album = models.Album.objects.filter(id=params_list[0])
        album.delete()

        return Response({"mesagge": "Album was deleted"})
