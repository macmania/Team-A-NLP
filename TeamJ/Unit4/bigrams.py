import nltk
from ast import literal_eval as make_tuple
import nltk
from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
import os
from nltk.collocations import *
from nltk.corpus import PlaintextCorpusReader

def loadCommon():
	f = open('Unit4/Bigrams10k.txt', 'rb')
	lst = []
	for l in f.readlines():
		lst.append(make_tuple(l)) # parses tuple 
	return lst

def loadCustomStopList():
	f = open('Unit4/customStop.txt', 'rb')
	lst = []
	for l in f.readlines():
		lst.append(l.rstrip('\n')) # parses tuple 
	return lst

commonBigrams = loadCommon()


collection = PlaintextCorpusReader("CollectionSmall", '.*')
classevent = PlaintextCorpusReader("Islip13Rain", '.*')

finder = BigramCollocationFinder.from_words(collection.words())

classeventTokens = nltk.wordpunct_tokenize(collection.raw())
classEventBigrams = nltk.bigrams(classeventTokens)
classEventBigram_FD = nltk.FreqDist(classEventBigrams)

collectionTokens = nltk.wordpunct_tokenize(collection.raw())
collectionBigrams = nltk.bigrams(collectionTokens)
collectionBigrams_FD = nltk.FreqDist(collectionBigrams)

collectionCommonBigrams = {}



for bigram in commonBigrams:
	if bigram in collectionBigrams_FD:
		collectionCommonBigrams[bigram] = collectionBigrams_FD[bigram]

for b in sorted(collectionCommonBigrams.items(), key=lambda x: x[1], reverse=True):
	print '%s\t%s' % b

from nltk.corpus import stopwords
count = 0
top300NOStop = []
for b in sorted(collectionCommonBigrams.items(), key=lambda x: x[1], reverse=True):
	if count == 300:
		break;
	if b[0][0] not in stopwords.words() and b[0][1] not in stopwords.words():
		top300NOStop.append(b)
		count += 1


collectionSmall_nostop = collection.words()
collectionSmall_nostop = [w for w in collectionSmall_nostop if len(w) > 3]

collectionSmall_FD = nltk.FreqDist(collectionSmall_nostop)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def checkCustomStop(word):
	for s in customStop:
		if s in word.lower():
			return True
	return False

count = 0
top300smallNOStop = []
customStop = loadCustomStopList();
for b in sorted(collectionSmall_FD.items(), key=lambda x: x[1], reverse=True):
	if count == 300:
		break;
	if b[0] not in stopwords.words() and b[0].isalpha() and len(b[0]) < 15 and is_ascii(b[0]) and not checkCustomStop(b[0]):
		top300smallNOStop.append(b)
		count += 1

for i in top300smallNOStop:
	print '\"%s\"' % i[0].lower()
