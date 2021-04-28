from rest_framework import viewsets
from rest_framework.response import Response
from base64 import b64encode
from .. import serializer
from .. import models


class ArtistViewset(viewsets.ModelViewSet):

    serializer_class = serializer.ArtistSerializer

    def get_queryset(self):

        artist_data = models.Artist.objects.all()
        return artist_data

    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('-')

        # if len(params_list) == 1:
        artist = models.Artist.objects.filter(
            id=params_list[0])  # filtrando por id
        data_serialize = serializer.ArtistSerializer(artist, many=True)
        return Response(data_serialize.data)

    def create(self, request, *args, **kwargs):
        artists_data = request.data
        encoded = b64encode(artists_data['name'].encode()).decode('utf-8')

        new_artist = models.Artist.objects.create(name=artists_data['name'],
                                                  identificador=encoded,
                                                  age=artists_data['age'],
                                                  albums=artists_data['albums'],
                                                  tracks=artists_data['tracks'],
                                                  myself=artists_data['myself'],)

        new_artist.save()
        data_serialize = serializer.ArtistSerializer(new_artist)
        return Response(data_serialize.data)

    def destroy(self, request, *args, **kwargs):
        params = kwargs['pk']
        params_list = params.split("-")
        artist = models.Artist.objects.filter(id=params_list[0])
        artist.delete()

        return Response({"mesagge": "Artist was deleted"})
