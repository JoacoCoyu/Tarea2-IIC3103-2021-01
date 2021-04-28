from rest_framework import viewsets
from rest_framework.response import Response
from base64 import b64encode
from .. import serializer
from .. import models


class ArtistAlbumViewset(viewsets.ModelViewSet):

    serializer_class = serializer.AlbumSerializer

    def get_queryset(self, artist_id):

        print(artist_id)
        #album_data = models.Album.objects.all()
        return "doing get"

    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])
        #params_list = params['pk'].split('-')
        return Response({"ruta en construccion"})
