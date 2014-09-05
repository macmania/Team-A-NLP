from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
from nltk.book import *
from nltk.stem.porter import *



listOfTexts= [text1,text2,text3,text4,text5,text6,text8,text9]


stemmer = PorterStemmer()
processedWords7 = [(stemmer.stem(word).lower()) for word in text7 if word.isalpha()]
fdist7 = FreqDist(processedWords7)

processedListOfTexts = []
for text in listOfTexts:
    processedWords = [(stemmer.stem(word)).lower() for word in text if word.isalpha()]
    for word in processedWords:
        processedListOfTexts.append(word)


setOfProcessedWords = set(processedListOfTexts)
masterDist = FreqDist(processedListOfTexts)
stopWords = []
for key in masterDist.keys():
    if masterDist[key] > 750:
        stopWords.append(key)

for word in fdist7.most_common(75):
    if word[0] not in stopWords:
        print(word[0])

print('\nCollocations')
colloc = text7.collocations();
