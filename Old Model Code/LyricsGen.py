from MCGraph import Graph
# from lyricsgenius import Genius # https://github.com/johnwmillr/LyricsGenius
# from decouple import config
from enum import Enum
from pathlib import Path
import re
import string
import os

import pprint                           # for debugging
pp = pprint.PrettyPrinter(indent=4)     # for debugging

# Setup genius API -- ensure you set the corresponding env variable to generated token
# token = config('GENIUS_ACCESS_TOKEN')
# genius = Genius(token)
# genius.remove_section_headers = True

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

class Genre(Enum):
    COUNTRY = "country"
    POP = "pop"
    RAP = "rap"
    ROCK = "rock"
    XMAS = "xmas"

def makeGraph(genre):
    """
    Constructs and returns the graph used to generate the lyrics. Returns None if input is not an instance of Genre
    """
    if not isinstance(genre, Genre):
        return None
    songSource = Path("sampleSongs")
    genreFolder = songSource / genre.name
    songNum = len([name for name in os.listdir(genreFolder)])
    lyricsList = []

    for i in range(songNum):
        song = genreFolder / '{}.txt'.format(i)
        with open(song) as f:
            lyricsList.append(clean(f.read()))
    return Graph(lyricsList)
    
g = makeGraph(Genre.XMAS)

# # To be replaced when I integrate Genius API
# # Subtract one for ds.store
# songNum = len([name for name in os.listdir('sampleSongs')]) - 1
# lyricsList = []

# # Process all songs
# for i in range(songNum):
#     with open('sampleSongs/{}.txt'.format(i), 'r') as f:
#         lyricsList.append(clean(f.read()))

# g = Graph(lyricsList)


""" Generate Markov Chaining Lyrics """
print(g.generateLyrics(200))

""" Generate LSTM Lyrics """
# Not yet implemented

""" Check Prob Dictionary """
# for lst in g.nextWordProbDict.values():
#     lst = lst.sort()
# pp.pprint(g.nextWordProbDict)

""" Test Clean Method """
# with open('sampleSongs/2.txt') as f:
#     print(clean(f.read()))

""" Test API Works """
# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
# print(artist.songs)