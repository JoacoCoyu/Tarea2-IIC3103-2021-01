from django.urls import path
from music_app import views
from music_app.app_views import artists, albums

urlpatterns = [
    path('home', views.homePageView, name='home'),
    path('artists', artists.artists, name='artists'),
    path('artists/<str:artist_id>', artists.artists_detail, name='artist_detail'),
    path('artists/<str:artist_id>/albums',
         albums.artists_albums, name='artist_album_detail'),
    # path('busqueda/', views.busqueda, name='busqueda'),
    # path('<str:serie>/<str:id_temporada>/', views.temporada, name='temporada'),
]
