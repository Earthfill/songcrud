from django.http import JsonResponse
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from musicapp.models import Artiste, Song


# Create your views here.
@api_view(["GET", "POST"])
def artiste_list_api(request):
    if request.method == "GET":
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        print(serializer.data)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == "POST":
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def song_list_api(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        print(serializer.data)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST", "PUT", "DELETE"])
def song_detail_api(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({"message":"Song not found"}, status=HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SongSerializer(song)
        print(serializer.data)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer = SongSerializer(Song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        song.delete()
        return Response({"message":"Song deleted"}, status=HTTP_204_NO_CONTENT)

