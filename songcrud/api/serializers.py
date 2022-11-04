from rest_framework import serializers

from musicapp.models import Artiste, Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ["first_name", "last_name"]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "date_released"]
        