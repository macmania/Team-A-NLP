'''
	Separates the text in ClassEvent sentences and tags them in the appropriate
  manner.
'''
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
import sys, os
######################sets up the path######
currPath = os.path.abspath("")
startPath = 0
endPath = len(currPath) - 1
pathSrc = currPath[0:endPath-9] + '/lib/src/'
pathClass = currPath[0:endPath-9] + '/lib/ClassCode/'
sys.path.append(pathSrc)
sys.path.append(pathClass)
from FilterFiles import extractTxtArticle, removeStopWords
from AnalysisWords import getFreqDist
##########################################



#a text of body that needs to
def getTagCorpus(textToks):
  listOfAllTags, listOfTags = [], []
  for txt in textToks:
    toks = nltk.word_tokenize(txt)
    tags = nltk.pos_tag(toks)
    listOfTags.append(tags)
    for t in tags:
      listOfAllTags.append(t)

  print listOfAllTags
  return listOfAllTags

#compares the list when there are nouns that are filtered
#and ones that are not filtered
def getNouns(listTags):
  setOfAllNouns = [a.lower() for (a, b) in listTags if b[0] == 'N' and b != "NUM" and len(a) > 2]
  return setOfAllNouns

#returns summary of the tags based on:
#  1. FreqDist
#  2. Not in Stop Words
def getPOS(listOfNouns):
  distNouns = getFreqDist(listOfNouns, 10)
  swFreeNouns = removeStopWords(distNouns)
  #print swFreeNouns
  return swFreeNouns

#need a better name
def analysis():

  CEcorpus_root = '../../lib/Corpus/ClassEvent'
  CEWordLists = PlaintextCorpusReader(CEcorpus_root, ".*\.txt")
  CE = CEWordLists.raw()
  sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  extractTxt = extractTxtArticle(CE)
  CE = "".join(extractTxt)
  CEsents = sent_tokenizer.tokenize(CE)

  listOfAllTags = getTagCorpus(CEsents)
  topNouns = getNouns(listOfAllTags)
  posSum = getPOS(topNouns)

  print "These are the list of all nouns in the class event corpus\n", len(posSum)
  for x in posSum:
    print x




analysis()
