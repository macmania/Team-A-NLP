'''
  Generic library that helps with analysis of the text
'''
import nltk
from nltk.probability import *
from collections import Counter

#returns a list of words based on how often they occur in the collections
def getFreqDist(text, occurNum):
  dictItems= FreqDist(text)
  topChoices = [a for (a, b) in dictItems.items() if b > occurNum]

  #if there are fewer than 25 items in the top choices, then return items that are in the
  #top 25 in the dictionary freq dist items
  if len(topChoices) < 25:
    topChoices = topChoices[0:25]
  print topChoices
  return topChoices

def getReducerFreqDist(freqdistr, listOfWords, occurNum):
  dictOfWords={}
  for word in listOfWords:
    dictOfWords[word]=freqdistr[word]
  topChoices = [a for (a, b) in dictOfWords.items() if b > occurNum]

  #if there are fewer than 25 items in the top choices, then return items that are in the
  #top 25 in the dictionary freq dist items
  if len(topChoices) < 25:
    topTuple = Counter(dictOfWords).most_common(25)
    topChoices= topTuple[0:25]
  print '------------------------------\nOutput from getReducerFreqDist\n'
  #print topDict
  print topChoices
  return topChoices
  
