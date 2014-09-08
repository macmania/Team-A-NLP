'''
	Extracts the appropriate corpus characteristics of the classevent text 
'''

from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown
import nltk

corpus_root = 'Islip13Rain'
worldlists = PlaintextCorpusReader(corpus_root, '.*')

print worldlists.fileids()
print len(worldlists.sents())

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() 
	for word in brown.words(categories=genre))
print cfd