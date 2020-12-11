from django.db import models
from Genre import Genre
import LyricsGen

popGraph = LyricsGen.makeGraph(Genre.POP)
countryGraph = LyricsGen.makeGraph(Genre.COUNTRY)
rapGraph = LyricsGen.makeGraph(Genre.RAP)
rockGraph = LyricsGen.makeGraph(Genre.ROCK)
xmasGraph = LyricsGen.makeGraph(Genre.XMAS)

# Create your models here.
class Pop(models.Model):
    lyrics = models.CharField(max_length=10000)

class Country(models.Model):
    lyrics = models.CharField(max_length=10000)

class Rap(models.Model):
    lyrics = models.CharField(max_length=10000)

class Rock(models.Model):
    lyrics = models.CharField(max_length=10000)

class Xmas(models.Model):
    lyrics = models.CharField(max_length=10000)
