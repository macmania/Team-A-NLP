'''
Summaries comparing your corpus with both ClassEvent and Baseline (see below)
To prepare for that:
Follow p. 51 so you can load YourSmall into NLTK.
Build a baseline English collection to help determine differences. This is the 
union of the 4 listed below, so you have a representative English collection. 
Call this Baseline. Include:
Brown Corpus, p. 42
Reuters Corpus, p. 44
Words Corpus, p. 60
State of the Union(state_union) Corpus, in list p. 47
Print the cumulative word length distribution, p. 48
Print a table with a column for each of the 3 corpora (i.e., ClassEvent, YourSmall, and Baseline), 
and a row for each word in YourWords, with entries giving the percentages of all word occurrences 
in that corpus that are for each word in YourWords (see textbook Section 2.2)
'''

import nltk
from nltk.corpus import wordnet
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

# corpus_root = '~/TexasExtractedFiles'
# wordlists = PlaintextCorpusReader(corpus_root, '.*')


'''
	print the set of WordNet synsets that cover all entries in YourWords
	print of YourWordsSynsets, but adding in the definition of each synset
'''
def PrintYourWordsSynsets(yourWords): 
	yourWordSynsets, tempSynset, wordSynsets = [], [], [] 
	yourWords = [w.split('\n')[0] for w in yourWords]
	for w in yourWords: 
		#wordSynsets.append(w.split('\n')[0])
		temp = wn.synsets(w)
		yourWordSynsets.append(temp)
		wordSynsets.append(w)
		for synset in temp:
			wordSynsets.append({synset.name.split('.')[0]:synset.definition})
	#for synset in tempSynset: 
		#wordSynsets.append({synset.name.split('.')[0]:synset.definition})
	return yourWordSynsets


'''
Print YourWordsLemmas: the set of words (lemmas) in any of 
YourWordsSynsets 
'''
def PrintWordLemmas(yourWordSynsets): 
	yourWordLemmas = [] 
	for word in yourWordSynsets: 
		print len(word)
		for w in word: 
			if type(w) is not list:
				print w
				yourWordLemmas.append(w.lemma_names)
	print yourWordLemmas


'''
Print the table above (i.e., with a column for each of the 3 corpora), using YourWordsLemmas instead of YourWords for the rows
'''
def PrintTable(classEvent, smallEvent, Baseline): 
	print table



f = open('YourWords')
lines = f.readlines() 
yourWordSynsets = PrintYourWordsSynsets(lines)
PrintWordLemmas(yourWordSynsets)