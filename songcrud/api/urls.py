from django.urls import path

from .views import artiste_list_api, song_list_api, song_detail_api

urlpatterns = [
    path("artistes/", artiste_list_api, name="artiste_list_api"),
    path("songs/<int:id>/", song_detail_api, name="song_detail_api"),
    path("songs/", song_list_api, name="song_list_api"),
]
