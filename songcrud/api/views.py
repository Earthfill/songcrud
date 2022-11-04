from django.http import JsonResponse
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from musicapp.models import Artiste, Song


# Create your views here.
@csrf_exempt
def artiste_list_api(request):
    if request.method == "GET":
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def song_list_api(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def song_detail_api(request, api):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return JsonResponse({"message":"Song not found"}, status=404)
    if request.method == "GET":
        serializer = SongSerializer(song)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=200)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SongSerializer(Song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        song.delete()
        return JsonResponse({"message":"Song deleted"}, status=204)

