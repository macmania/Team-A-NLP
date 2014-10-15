from __future__ import division
import nltk
from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
import os
from nltk.corpus import PlaintextCorpusReader
collection = PlaintextCorpusReader("CollectionSmall", '.*')
classevent = PlaintextCorpusReader("Islip13Rain", '.*')
classwordsloweralpha = [w.lower() for w in classevent.words() if w.isalpha()]

def avgWordLength(wordlists):
	return sum([len(w) for w in wordlists.words()]) / len(wordlists.words())

def averageSentLength(wordlists):
	return sum(len(s) for s in wordlists.sents()) / len(wordlists.sents())

def averageReadabilityIndex(wordlists):
	return 4.71*avgWordLength(wordlists) + 0.5*averageSentLength(wordlists) - 21.43



wordslower = [w.lower() for w in collection.words()]
wordsloweralpha = [w for w in wordslower if w.isalpha()]
freq5 = FreqDist([w for w in wordsloweralpha if len(w) > 5])
freq7 = FreqDist([w for w in wordsloweralpha if len(w) > 7])

bfreq = FreqDist([b for b in bigrams(wordsloweralpha) if len(b[0]) > 3 and len(b[1]) > 3 ])

avgWordLength(collection)
averageSentLength(collection)
averageReadabilityIndex(collection) #8.09414833134974

wordlenNoPunc = sum([len(w) for w in wordsloweralpha]) / len(wordsloweralpha)
ariNoPunc = 4.71*5.254275553161502 + 0.5*17.807400404056487-21.43 # 12.221338057418919

def printFreqDistForLen15(words):
	for i in range(1, 16):
		print(i,": ", len([w for w in words if len(w) == i]) / len(words))

alphalowerfreq = FreqDist(wordsloweralpha)
ourwords = ["shooting", "elementary", "school", "dead", "victim", "gunman", "connecticut", "sandy", "injured", "lanza", "tragedy", "grade", "children", "firearm", "weapon", "morning", "december", "teacher", "police", "motive"];

for i in range(0, len(ourwords)):
	print(str(ourwords[i])+ ": "+ str(alphalowerfreq[ourwords[i]] / len(wordsloweralpha)))

from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.corpus import state_union
from nltk.corpus import words

setnames = ["baseline", "Class Event", "Connecticut School Shooting"]

baselineNOSET = brown.words() + reuters.words() + state_union.words() + words.words();
baseline = set(baselineNOSET) #nltk.Text(corpuses)
sets = {"baseline":baseline , "Class Event":set(classwordsloweralpha), "Connecticut School Shooting":set(wordsloweralpha)}
setlens = {"baseline":sum(map(lambda x: len(x), baseline)) , "Class Event":sum(map(lambda x: len(x), set(classwordsloweralpha))), "Connecticut School Shooting":sum(map(lambda x: len(x), set(wordsloweralpha)))}


cfd = nltk.ConditionalFreqDist((s, len(word)) 
	for s in setnames 
	for word in sets[s])
cpd = nltk.ConditionalProbDist(
	(s, len(word)) 
	for s in setnames 
	for word in sets[s])
cfd.plot(cumulative=True)

baselinefreq = FreqDist([w.lower() for w in baselineNOSET if w.isalpha()])
classeventfreq = FreqDist(classwordsloweralpha)

print("Our Words\tBaseline\tClass Event\tConnecticut School Shooting")
for w in ourwords:
	print(w + "\t" + str(baselinefreq[w] / len(baseline)) + "\t" + str(classeventfreq[w] / len(classwordsloweralpha)) + "\t" + str(alphalowerfreq[w] / len(wordsloweralpha)))

from nltk.corpus import wordnet as wn
wn.synsets('motorcar')

l = set()
for w in ourwords:
	l |= set(wn.synsets(w))

for s in l:
	print(str(s) + ": " + s.definition())

lemmas = set()
for synset in l:
	lemmas |= set(synset.lemma_names())
	for lemma in set(synset.lemma_names()):
		print(str(synset) + ": " + lemma);

print("Our Words\tBaseline\tClass Event\tConnecticut School Shooting")
for w in lemmas:
	print(w + "\t" + str(baselinefreq[w] / len(baseline)) + "\t" + str(classeventfreq[w] / len(classwordsloweralpha)) + "\t" + str(alphalowerfreq[w] / len(wordsloweralpha)))

# find amount of words not in stoplist
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
withoutstoplist = [w for w in classwordsloweralpha if w not in stoplist]
len(withoutstoplist) / len(classwordsloweralpha)
