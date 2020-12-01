from WordGraph import Graph
import re
import string
import os

import pprint                           # for debugging
pp = pprint.PrettyPrinter(indent=4)     # for debugging

# deal with Genius API here
# For now I'll just work with the copy and pasted lyrics from Genius

def clean(lyricsString):
    """
    Remove unnecessary annotations and make lyrics lowercase
    """
    lyricsString = re.sub(r'\[(.+)\]', ' ', lyricsString)
    # lyricsString = ' '.join(lyricsString.split())
    lyricsString = lyricsString.lower()
    lyricsString = lyricsString.translate(str.maketrans('', '', string.punctuation))
    return lyricsString

# Subtract one for ds.store
songNum = len([name for name in os.listdir('sampleSongs')]) - 1
lyricsList = []
# Process all songs
for i in range(songNum):
    with open('sampleSongs/{}.txt'.format(i), 'r') as f:
        lyricsList.append(clean(f.read()))

g = Graph(lyricsList)
print(g.generateLyrics(50))
# pp.pprint(g.nextWordProbDict)