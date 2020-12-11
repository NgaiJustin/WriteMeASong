from MCGraph import Graph
from lyricsgenius import Genius # https://github.com/johnwmillr/LyricsGenius
from decouple import config
import re
import string
import os

import pprint                           # for debugging
pp = pprint.PrettyPrinter(indent=4)     # for debugging

# Setup genius API -- ensure you set the corresponding env variable to generated token
token = config('GENIUS_ACCESS_TOKEN')
genius = Genius(token)
genius.remove_section_headers = True

# Find way to get a list of song names for top songs of a particular genre
#   Option 1: Spotify:
#       - python api --> Spotify
#       - Use "get a category" endpoint to get list of songs
#           - https://developer.spotify.com/documentation/web-api/reference-beta/#endpoint-get-a-category
#       - May need some work
#   Option 2: Itunes?

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

# To be replaced when I integrate Genius API
# Subtract one for ds.store
songNum = len([name for name in os.listdir('sampleSongs')]) - 1
lyricsList = []

# Process all songs
for i in range(songNum):
    with open('sampleSongs/{}.txt'.format(i), 'r') as f:
        lyricsList.append(clean(f.read()))

g = Graph(lyricsList)


""" Generate Markov Chaining Lyrics """
# print(g.generateLyrics(100))

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