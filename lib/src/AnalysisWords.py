'''
  Generic library that helps with analysis of the text
'''
import nltk
from nltk.probability import *


#returns a list of words based on how often they occur in the collections
def getFreqDist(text, occurNum):
  listText = FreqDist(text)
  dictItems = listText.items()
  topChoices = [a for (a, b) in dictItems if b > occurNum]

  #if there are fewer than 25 items in the top choices, then return items that are in the
  #top 25 in the dictionary freq dist items
  if len(topChoices) < 25:
    listWords = dictItems[0:26]
    print listWords
    topChoices = [a for (a, b) in listWords]

  return topChoices
