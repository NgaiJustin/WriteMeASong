from django.shortcuts import render
from rest_framework import generics, status
from .models import Song
from .serializers import SongSerializer, CreateSongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SongView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class CreateSongView(APIView):
    serializer_class = CreateSongSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            length = serializer.data.get('length')
            genre = serializer.data.get('genre')
            
            # Only keep the most recently generated song
            # so we don't flood db
            queryset = Song.objects.filter(tag=1)
            if queryset.exists():
                song = queryset[0]
                song.genre = genre
                song.length = length
            else:
                song = Song(length= length, genre= genre)
                song.save()
            song.genLyrics(genre)
            return Response(SongSerializer(song).data, status=status.HTTP_201_CREATED)
            
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)