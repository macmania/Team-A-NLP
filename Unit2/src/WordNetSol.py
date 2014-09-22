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

import time
import nltk
from nltk.corpus import *
from nltk.probability import *
from nltk.corpus import wordnet
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

'''
	print the set of WordNet synsets that cover all entries in YourWords
	print of YourWordsSynsets, but adding in the definition of each synset
'''
def PrintYourWordsSynsets(yourWords):
	yourWordSynsets, tempSynset, wordSynsets = [], [], []
	yourWords = [w.split('\n')[0] for w in yourWords]
	for w in yourWords:
		temp = wn.synsets(w)
		yourWordSynsets.append(temp)
		wordSynsets.append(w)
		for synset in temp:
			wordSynsets.append({synset.name().split('.')[0]:synset.definition})
	print wordSynsets, '\n', yourWordSynsets

	return yourWordSynsets


'''
Print YourWordsLemmas: the set of words (lemmas) in any of
YourWordsSynsets
'''
def PrintWordLemmas(yourWordSynsets):
	yourWordLemmas, wordLemmas = [], []
	for word in yourWordSynsets:
		for w in word:
			if type(w) is not list:
				yourWordLemmas.append(w.lemma_names)
	for l in yourWordLemmas:
		if type(l) is list:
			for x in l:
				if x not in wordLemmas:
					wordLemmas.append(x)
				else:
					wordLemmas.append(x)

	print yourWordLemmas
	return wordLemmas


'''
Print the table above (i.e., with a column for each of the 3 corpora),
using YourWordsLemmas instead of YourWords for the rows
'''
def PrintTable(lemmasBrown, lemmasIsSlip, lemmas):
    fil = open('../output/lemmas.txt','w')
    fil.write(str(lemmas))
    fil.close()


    fi = open('../output/lemmasIsSlip.txt', 'w')
    fi.write(str(lemmasIsSlip))
    fi.close()

    f = open('../output/lemmas.txt')
    textLemmas = f.read().lower()
    lemmaList = textLemmas[1:len(textLemmas)-3].split(',')
    f.close()

    filesSlip = open('../output/lemmasIsSlip.txt')
    fSlip = filesSlip.read().lower()
    lemmaListSlip = fSlip[1:len(fSlip)-3].split(',')

    f = open('../output/ALLRAW.txt')
    baseText = f.read().lower()
    baseList = str((baseText[1:len(baseText)-3]).split())[1:len(baseText)-3].split(',')

    baselineFdist=FreqDist(baseList)

    f = open('../output/ISLIPPROCESSED.txt')
    isliptext = f.read().lower()
    isliplist = (isliptext[1:len(isliptext)-3]).split(',')


    classEventFdist=FreqDist(isliplist)
    #time.sleep(10)
    f = open('../output/TEXASPROCESSED.txt')
    text = f.read().lower()

    texasEvent= (text[1:len(text)-3].split(','))

    texasEventFdist=FreqDist(texasEvent)
    cfdist = ConditionalFreqDist()
    corporaDist=[classEventFdist, texasEventFdist, baselineFdist]

    allLemmas = lemmaListSlip + lemmaList
    for word in allLemmas:
        baseVal=baselineFdist[word]
        classVal=classEventFdist[word]
        texasVal = texasEventFdist[word]
        print('word: ' + word + ' classVal: ' + str(classVal) + ' baseVal: ' +  str(baseVal) + ' texasVal: ' + str(texasVal))


f = open('../output/YourWords')
fIsSlip = open('../output/YourWordsIsSlip')
linesIsSlip = fIsSlip.readlines()
lines = f.readlines()

yourWordSynsets = PrintYourWordsSynsets(lines)
yourWordSynsetsLemmas = PrintYourWordsSynsets(linesIsSlip)
lemmasTexas = PrintWordLemmas(yourWordSynsets)
lemmasIsSlip = PrintWordLemmas(yourWordSynsetsLemmas)

print lemmasIsSlip, lemmasTexas
PrintTable([], lemmasIsSlip, lemmasTexas)
