from django.contrib import admin
from django.urls import path, include

from .views import homePageView, getAllArtist

urlpatterns = [
    path('', homePageView, name='home'),
    path('artists/', getAllArtist, name='all_artists'),
]