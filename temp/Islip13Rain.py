'''
	Temp file to scrape useless noise from Texas */*.txt files
'''

import glob
import errno
import nltk
from nltk import FreqDist
from nltk.collocations import *
import operator
from nltk.corpus import PlaintextCorpusReader

#returns a list of top 10 most frequent words
def extractTopWrds(strTxt):
	strTxt = [t.lower() for t in strTxt if len(t) > 3]
	strTxt = nltk.FreqDist(strTxt)
	sortedDictTxt = sorted(strTxt.iteritems(), key=operator.itemgetter(1))

	return sortedDictTxt[len(sortedDictTxt)-10:len(sortedDictTxt)]

#returns a list of phrases that occur the most, may need to change it up
#still need to be examined a bit closely
def extractPhrases(strTxt):
	tokens = nltk.wordpunct_tokenize(str(strTxt))
	tokens = [t.lower() for t in tokens if len(t) > 3]
	pairs = nltk.bigrams(tokens)

	#1 Overview of using collocations
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	trigram_measures = nltk.collocations.TrigramAssocMeasures()
	finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
	f2 = nltk.collocations.BigramCollocationFinder.from_words(pairs)
	for i in range(2, 6): 
		f2.apply_freq_filter(i)
	scored = finder.score_ngrams(bigram_measures.raw_freq)
	word_fd = nltk.FreqDist(tokens)
	bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
	finder = BigramCollocationFinder(word_fd, bigram_fd)
	#need to be examined which one is better
	print sorted(finder.nbest(trigram_measures.raw_freq, 2))
	print sorted(finder.nbest(trigram_measures.raw_freq, 3))
	return sorted(finder.nbest(trigram_measures.raw_freq, 3))

#Texas folder collocation start
corpus_root = "../Islip13Rain"
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
ClassEvent = nltk.Text(wordlists.words())
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
extractTxt = ' '
topWords = extractTopWrds(ClassEvent)
phrases = extractPhrases(ClassEvent)

print topWords
print phrases
