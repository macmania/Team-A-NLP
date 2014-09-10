<<<<<<< HEAD:U1_Colloc.py
'''
	Collocation portion for text7
'''

import nltk
from nltk import FreqDist
import string
from nltk.collocations import *
from nltk.book import *
import glob
import errno

#starts parsing the text file

tokens = nltk.wordpunct_tokenize(str(text7))
tokens = [t.lower() for t in tokens if len(t) > 3]
pairs = nltk.bigrams(tokens)
texasAllPairs = [] 

#print pairs

#1 Overview of using collocations
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
f2 = nltk.collocations.BigramCollocationFinder.from_words(pairs)
for i in range(2, 6): 
	f2.apply_freq_filter(i)


#2 Finders
scored = finder.score_ngrams(bigram_measures.raw_freq)
word_fd = nltk.FreqDist(tokens)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
finder = BigramCollocationFinder(word_fd, bigram_fd)
print sorted(finder.nbest(trigram_measures.raw_freq, 3)) # sorted(bigram for bigram, score in scored)
exclude = set(string.punctuation)

fdist1 = FreqDist(tokens)

finder = TrigramCollocationFinder.from_words(tokens)
print sorted(finder.nbest(trigram_measures.raw_freq, 4))


#Texas folder collocation start
files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
for name in files: 
	try: 
		with open(name) as f: 
			tok = nltk.bigrams(f.read())
			tok = [t.lower() for t in tok if len(t) > 3]
			pair = nltk.bigrams(tok)
			finder = TrigramCollocationFinder.from_words(tokens)
			texasAllPairs.append(finder.nbest(trigram_measures.raw_freq, 4))
	except IOError as exc: 
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.

print texasAllPairs


=======
'''
	Collocation portion for text7
'''

import nltk
from nltk import FreqDist
import string
from nltk.collocations import *
from nltk.book import *
import glob
import errno

#starts parsing the text file

tokens = nltk.wordpunct_tokenize(str(text7))
#tokens = [t.lower() for t in tokens]
pairs = nltk.bigrams(tokens)
texasAllPairs = [] 

#print pairs

#1 Overview of using collocations
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(text7)
f2 = nltk.collocations.BigramCollocationFinder.from_words(pairs)
for i in range(2, 6): 
	f2.apply_freq_filter(i)


#2 Finders
scored = finder.score_ngrams(bigram_measures.raw_freq)
word_fd = nltk.FreqDist(tokens)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
finder = BigramCollocationFinder(word_fd, bigram_fd)
print sorted(finder.nbest(bigram_measures.raw_freq, 10)) # sorted(bigram for bigram, score in scored)
exclude = set(string.punctuation)

fdist1 = FreqDist(tokens)

finder = TrigramCollocationFinder.from_words(tokens)
#print sorted(finder.nbest(trigram_measures.raw_freq, 4))




>>>>>>> FETCH_HEAD:Unit1/Text7Colloc.py
