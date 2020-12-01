from collections import defaultdict as dd
import string
import random

class Graph:
    nextWordProbDict = {}
    lyrics = ""

    def __init__(self, lstOfLyricsStrings):
        # lyricsString.translate(None, string.punctuation)
        # Maybe use the full stop to indicate newline: prettyPrint
        tempDefaultDict = dd(list)
        for lyricsString in lstOfLyricsStrings:
            lyricsString.lower()
            words = lyricsString.split(' ')
            for currWord, nextWord in zip(words[0:-1], words[1:]):
                tempDefaultDict[currWord].append(nextWord)
        self.nextWordProbDict = dict(tempDefaultDict)
    
    def read(self, lyricsString):
        lyricsString.lower()
        words = lyricsString.split(' ')
        tempDefaultDict = dd(list)
        for currWord, nextWord in zip(words[0:-1], words[1:]):
            tempDefaultDict[currWord].append(nextWord)

    def nextWord(self, currWord):
        """
        Returns a randomly selected next word based on the 
        current word
        """
        probDict = self.nextWordProbDict
        return random.choice(probDict[currWord])

    def generateLyrics(self, count=100):
        probDict = self.nextWordProbDict
        currWord = random.choice(list(probDict.keys()))
        currWord.capitalize()
        for __ in range(count):
            self.lyrics += currWord
            self.lyrics += " "
            currWord = self.nextWord(currWord)
        return self.lyrics

            

    

    