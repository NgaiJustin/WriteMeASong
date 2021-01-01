from collections import defaultdict as dd
import string
import random

class Graph:
    nextWordProbDict = {}
    lyrics = ""

    def __init__(self, lstOfLyricsStrings):
        tempDefaultDict = dd(list)
        for lyricsString in lstOfLyricsStrings:
            lyricsString = lyricsString.lower()
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

    def clean(self, lyricsString):
        """
        Remove extra space from newLine and newParagraph seperators
        """
        lyricsString = lyricsString.replace(' \n ', '\n')
        lyricsString = lyricsString.replace(' \n\n ', '\n\n')
        return lyricsString

    def generateLyrics(self, count=100):
        self.lyrics = ""
        probDict = self.nextWordProbDict
        currWord = random.choice(list(probDict.keys()))
        while count:
            if '\n' in currWord:
                count += 1
            self.lyrics += currWord
            self.lyrics += " "
            currWord = self.nextWord(currWord)
            count -= 1
        return self.clean(self.lyrics)

            

    

    