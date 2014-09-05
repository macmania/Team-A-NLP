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
	return sortedDictTxt[len(sortedDictTxt)-5:len(sortedDictTxt)]

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

#extracts a chunk of text that are similar distance to one another, assuming that the
#article is double or single spaced. 
#returns the extracted text
'''Need to ask Dr. Fox what the best approach would be to classify a particular text: 
	according to the chunk it belongs to, but since for this program we are not classify
	the text on a particular file, we just want to know which content is the most relevant'''
def extractTxtArticle(strTxt):
	strTxt = strTxt.splitlines()
	extractTxt = []
	for r in range(len(lines)):
		if len(lines[r].strip(' ')) >= 80 and '|' not in lines[r] not in lines[r] and '#' not in lines[r]:
			extractTxt.append(lines[r])

	print extractTxt
	return extractTxt


#Texas folder collocation start
corpus_root = "Islip13Rain"
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
ClassEvent = nltk.Text(wordlists.words())
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
extractTxt = ' '
topWords = extractTopWrds(ClassEvent)
phrases = extractPhrases(ClassEvent)


'''
for name in files: 
	try: 
		with open(name) as f: 
			lines = f.read()
			if classifyTxt(lines):
				artcle += 1
				art.append(name)
				extractTxt = extractTxtArticle(lines)
	
			else: 
				extractTxt = lines.split()
				nonArtcl += 1
				nonArt.append(name)

			topWords = extractTopWrds(extractTxt)
			phrases = extractPhrases(extractTxt)

			print name[36:], topWords, phrases

	except IOError as exc: 
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.

'''
