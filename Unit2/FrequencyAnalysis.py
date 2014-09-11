from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
from nltk.book import *
from nltk.stem.porter import *


print('Starting creation of stop words')

stopWords = []
mitStopWordsFile = open('mit_stop_words.txt')
stopWords = [line.strip() for line in mitStopWordsFile]
mitStopWordsFile.close()

print('Done creating stop words')


#Populate the list of texts to be used
listOfTexts = []
files = glob.glob("TexasExtractedFiles/*.txt")
count = 0
for f in files:
	raw = f.read()
	#TOKENIZE??????????????????
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	listOfTexts.append(text)
	count = count + 1
	if (count % 50 == 0)
		print(count)





stemmer = PorterStemmer()
processedWords7 = [(stemmer.stem(word).lower()) for word in text7 if word.isalpha()]
fdist7 = FreqDist(processedWords7)

processedListOfTexts = []
for text in listOfTexts:
    processedWords = [(stemmer.stem(word)).lower() for word in text if word.isalpha()]
    for word in processedWords:
        processedListOfTexts.append(word)

print('Done stemming and stuff')

setOfProcessedWords = set(processedListOfTexts)
masterDist = FreqDist(processedListOfTexts)
'''
stopWords = []
for key in masterDist.keys():
    if masterDist[key] > 750:
        stopWords.append(key)
'''


#Use items() because most_common() doesn't work on mac
for word in fdist7.items()[:75]:
    if word[0] not in stopWords:
        print(word[0])

