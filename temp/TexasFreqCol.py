'''
	Temp file to scrape useless noise from Texas */*.txt files
'''

import glob
import errno
import nltk

#analyzes the text based on the number of lines in comparison to the words of a text file
#if there are more lines than text then it's not an article. (Interesting to look at whether a
#	cluster of text may indicate that the text is an article)
#If it's an article then we use a k-means clustering to look at: 
#	- top 10 most frequent words
#	- top collocation phrases	
#If it's not an article then we report:
#	- top 5 most frequent words
#	- find the common phrases
#Question: which one is better? common phrases for an article or most frequent words in 
#																	a non-article
def classifyTxt(strTxt):
	if strTxt == None: 
		print "parameter cannot be empty"
	else:
		numNewLines = 0
		for c in strTxt: 
			if c == '\n':
				numNewLines += 1
		if numNewLines < len(strTxt.split()) and numNewLines != 0:
			return True
		else: 
			return False

#returns a list of top 10 most frequent words
def extractTopWrds(strTxt):
	dictTxt = nltk.FreqDist(dictTxt)
	sortedDictTxt = sorted(dictTxt.iteritems(), key=operator.itemgetter(1))
	return sortedDictTxt[len(sortedDictTxt)-5:len(sortedDictTxt)]

#returns a list of phrases that occur the most, may need to change it up
#still need to be examined a bit closely
def extractPhrases(strTxt):
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
def extractTxtArticle(strTxt):
	''' to-do stub'''
	return  ' '



#Texas folder collocation start
files = glob.glob("../Texas Fertilizer Plant Explosion/*.txt")
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
for name in files: 
	try: 
		with open(name) as f: 
			lines = f.read()
			if classifyTxt(lines):
				artcle += 1
				art.append(name)
			else: 
				nonArtcl += 1
				nonArt.append(name)

	except IOError as exc: 
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.

print artcle, nonArtcl
print art[0:5]
print nonArt[0:5]

