from music_app.views import CarSpecViewset
from music_app.app_views import artists, albums, artists_albums
#from rest_framework import routers
from rest_framework_nested import routers

router = routers.SimpleRouter()
#router.register('cars', CarSpecViewset, basename='cars_info')
router.register('artists', artists.ArtistViewset, basename='artists_info')
router.register('albums', albums.AlbumViewset, basename='albums_info')
router.register('artists/<int:artist_id>/albums',
                artists_albums.ArtistAlbumViewset, basename='artist_album_info')
