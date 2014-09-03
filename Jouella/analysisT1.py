'''
	analysis of Text 1 specified on the Unit I 
	some questions that we want to investigate: 
		- what is the best way to summarize with words or phrases considering frequencies
			+ are frequencies best way to effectively summarize a particular text? 
		- examples: text 7, ClassEvent
		- what we found from googling and also experimenting is that 
		making a text shorter (paraphrasing it), using key words, we can produce an ok 'summary' of
		it. 
		- the take away semantic analysis, pronoun recognition, etc. NLP stuff is fundamental in carefully
		analyzing text. We have to do more work when the text gets larger. 

		So in this presentation, wanted to share some of the stuff we found. The limitations that we 
		found when we looked at articles that contained length of text greater than 472 characters: 
			+ 472 characters
			+ 1000 characters
			+ 2000 characters
			+ 3000 characters - found that there is too much noise with the data so we get rid of useless
			stuff (the, a, an, etc. words <=3). So if we look at the 
				JLaw fiasco
				Is the cloud secure?
				- we find that frequency is bad, like really bad
				- here is data that we found
		So frequency is good when you have a small text such as > 1000 characters, probability will tell you 
		that 

		So after googling, reading stack overflow and what not, frequency is good to implement once you've limit
		the text - approximately 1000 according to this ACM Research paper. 


		Just a caveat, i've included an option when summarizing texts. 
'''


import nltk
from nltk import FreqDist
import string
from nltk.collocations import *

#starts parsing the text file
f = open("../Islip13Rain/7.txt")
tokens = nltk.word_tokenize(open("../Islip13Rain/7.txt").read())
tokens = [t.lower() for t in tokens if len(t) > 3]
pairs = nltk.bigrams(tokens)
#print pairs

#1 Overview of using collocations
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
f2 = nltk.collocations.BigramCollocationFinder.from_words(pairs)
for i in range(2, 6): 
	f2.apply_freq_filter(i)
	#print 'frequents ', i, f2.nbest(bigram_measures.pmi, 10)
#decreases in frequencies



#2 Finders
scored = finder.score_ngrams(bigram_measures.raw_freq)
word_fd = nltk.FreqDist(tokens)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
finder = BigramCollocationFinder(word_fd, bigram_fd)
print sorted(finder.nbest(trigram_measures.raw_freq, 3)) # sorted(bigram for bigram, score in scored)
exclude = set(string.punctuation)
#lines = ''.join(ch for ch in lines if ch not in exclude)
#print(sorted(lines))
#tokens = sorted(set(lines))
fdist1 = FreqDist(tokens)
#print (fdist1)


#finder = TrigramCollocationFinder.from_words(tokens)
finder = TrigramCollocationFinder.from_words(tokens)
print sorted(finder.nbest(trigram_measures.raw_freq, 4))

