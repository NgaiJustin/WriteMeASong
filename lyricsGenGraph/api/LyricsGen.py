from pathlib import Path
from Genre import Genre
from MCGraph import Graph
import re
import string
import os

def clean(lyricsString):
    """
    Format lyrics and remove unnecessary annotations
    """
    # Remove the [xxx] annotations
    lyricsString = re.sub(r'\[(.+)\]', ' ', lyricsString) 

    # Remove punctuations except ', ? and ! 
    toRemove = string.punctuation.replace('\'', '')
    toRemove = toRemove.replace('!', '')
    toRemove = toRemove.replace('?', '')
    lyricsString = lyricsString.translate(str.maketrans('', '', toRemove)) 

    # Format newLine and newParagraph seperators
    lyricsString = lyricsString.lower()
    lyricsString = lyricsString.replace('\n\n', 'NP')
    lyricsString = lyricsString.replace('\n', ' \n ')
    lyricsString = lyricsString.replace('NP', ' \n\n ')

    return lyricsString

def makeGraph(genre):
    """
    Constructs and returns the graph used to generate the lyrics. Returns None if input is not an instance of Genre
    """
    if not isinstance(genre, Genre):
        return None
    songSource = Path("songSource")
    genreFolder = songSource / genre.name
    songNum = len([name for name in os.listdir(genreFolder)])
    lyricsList = []

    for i in range(songNum):
        song = genreFolder / '{}.txt'.format(i)
        with open(song) as f:
            lyricsList.append(clean(f.read()))
    return Graph(lyricsList)