from MCGraph import Graph
import re
import string
import os

import pprint                           # for debugging
pp = pprint.PrettyPrinter(indent=4)     # for debugging

# deal with Genius API here
# For now I'll just work with the copy and pasted lyrics from Genius

def clean(lyricsString):
    """
    Format lyrics and remove unnecessary annotations
    """
    # Remove punctuations except '
    lyricsString = lyricsString.translate(str.maketrans('', '', string.punctuation.replace('\'', ''))) 

    # Format newLine and newParagraph seperators
    lyricsString = lyricsString.lower()
    lyricsString = lyricsString.replace('\n\n', 'NP')
    lyricsString = lyricsString.replace('\n', ' \n ')
    lyricsString = lyricsString.replace('NP', ' \n\n ')

    # Remove the [xxx] annotations
    lyricsString = re.sub(r'\[(.+)\]', ' ', lyricsString) 

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
print(g.generateLyrics(50))

""" Generate LSTM Lyrics """
# Not yet implemented

""" Check Prob Dictionary """
# for lst in g.nextWordProbDict.values():
#     lst = lst.sort()
# pp.pprint(g.nextWordProbDict)

""" Test Clean Method """
# with open('sampleSongs/2.txt') as f:
#     print(clean(f.read()))