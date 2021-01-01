from django.db import models
from .Genre import Genre
from . import LyricsGen

popGraph = LyricsGen.makeGraph(Genre.POP)
countryGraph = LyricsGen.makeGraph(Genre.COUNTRY)
rapGraph = LyricsGen.makeGraph(Genre.RAP)
rockGraph = LyricsGen.makeGraph(Genre.ROCK)
xmasGraph = LyricsGen.makeGraph(Genre.XMAS)

# Create your models here.

class Song(models.Model):
    tag = models.IntegerField(null=False, default=1)
    lyrics = models.CharField(max_length=10000, default='')
    genre = models.CharField(max_length=7)
    length = models.IntegerField(null=False, default=-1)

    def genLyrics(self, genre):
        if genre == 'pop':
            self.lyrics = popGraph.generateLyrics(self.length)
        elif genre == 'country':
            self.lyrics = countryGraph.generateLyrics(self.length)
        elif genre == 'rap':
            self.lyrics = rapGraph.generateLyrics(self.length)
        elif genre == 'rock':
            self.lyrics = rockGraph.generateLyrics(self.length)
        elif genre == 'xmas':
            self.lyrics = xmasGraph.generateLyrics(self.length)
        self.save()
    