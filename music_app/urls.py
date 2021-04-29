from django.urls import path
from music_app import views
from music_app.app_views import artists, albums, tracks

urlpatterns = [
    path('home', views.homePageView, name='home'),
    path('artists', artists.artists, name='all_artists'),
    path('artists/<str:artist_id>', artists.artists_detail, name='artist_detail'),
    path('artists/<str:artist_id>/albums',
         albums.artists_albums, name='artist_album_detail'),
    path('albums', albums.albums, name='all_albums'),
    path('albums/<str:album_id>', albums.albums_detail, name='album_detail'),
    path('albums/<str:album_id>/tracks',
         tracks.albums_tracks, name='album_track_detail'),
    path('tracks', tracks.tracks, name='all_tracks'),
    path('tracks/<str:track_id>', tracks.tracks_detail, name='album_detail'),
]
