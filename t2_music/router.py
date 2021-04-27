from music_app.views import CarSpecViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cars', CarSpecViewset, basename='cars_info')
