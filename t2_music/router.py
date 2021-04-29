from music_app.views import CarSpecViewset
from music_app.app_views import artists, albums, artists_albums
from rest_framework import routers
from django.urls import path
#from rest_framework_nested import routers as nested_routers
#from music_app.views import homePageView

router = routers.DefaultRouter()
#router.register('cars', CarSpecViewset, basename='cars_info')
router.register(r'artists', artists.ArtistViewset, basename='artists_info')
router.register('albums', albums.AlbumViewset, basename='albums_info')
# router.register('artists/<int:artist_id>/albums',
#                 artists_albums.ArtistAlbumViewset, basename='artist_album_info')

# urlpatterns = [
#     path('home/', homePageView, name='index'),
#     # path('episodio/<str:id_episodio>/', views.episodio, name='episodio'),
#     # path('personaje/<str:nombre>/', views.personaje, name='personaje'),
#     # path('busqueda/', views.busqueda, name='busqueda'),
#     # path('<str:serie>/<str:id_temporada>/', views.temporada, name='temporada'),
# ]
