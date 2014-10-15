'''
    Analysis of our frequent distribution for text 7
    removes the stop words and tracks the number of times a particular word has appeared 
    in a text
'''

from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
from nltk.book import *

class FrequentDistributionText7: 
    indicativeWords = list()
    fdist7 = []

    def __init__(self): 
        self.listOfTexts= [text1,text2,text3,text4,text5,text6]
        self.fdist7= nltk.FreqDist(text7)
        self.commonWords= self.fdist7.items() 

    def loadFreqText(self): 
        indicativeWords= [word[0] for word in self.commonWords if word[0].isalpha()]
        masterDictFreq = dict()
        for text in self.listOfTexts:
            fdist = FreqDist(text) #examine the frequent distribution for each text
            for word in fdist:
                if word in masterDictFreq.keys():
                    masterDictFreq[word] = masterDictFreq[word] + fdist[word] #add one when a word appears
                else:
                    masterDictFreq[word] =fdist[word]

        #sorts all of the items in all of the texts based on their values
        self.sortedDictInAllTxt = dict(sorted(masterDictFreq.items(), key=lambda x: x[1])[:50])


    def analyseText7(self): 
        allWordsIn7Txt = dict(sorted(self.fdist7.items(), key=operator.itemgetter(1)))
        text7DistCommon = dict()

        #get rid of words that are occuring in other text
        for common in allWordsIn7Txt:
            print common, type(common), type(self.sortedDictInAllTxt)
            if (common not in self.sortedDictInAllTxt and common in allWordsIn7Txt and allWordsIn7Txt[common] < 1500 and len(common) > 3):
                text7DistCommon[common] = allWordsIn7Txt[common]

        print text7DistCommon        
        

    def collocationTxt7(self): 
        colloc = text7.collocations();

        wordPercentList, textLength = [], len(text7)

        print (len(self.indicativeWords))
        #Implement stop word filters
        stopWords = (open('../StopWords/nltk_english_stopWords.txt')).read().split()
        for word in self.indicativeWords:
            if word in stopWords:
                print (word, ' found and removed')
                self.indicativeWords.remove(word)

        # word Is indeed indicative
        for word in self.indicativeWords:    
            wordPercentList.append(100 * text1.count(word) / textLength ) 
       
        print (len(self.indicativeWords)), (len(wordPercentList))

        print('\nPercentage list of all indicative words:\n')
        for i in range(0,len(self.indicativeWords)-1):
            print(self.indicativeWords[i],wordPercentList[i])

freqDist7 = FrequentDistributionText7()
freqDist7.loadFreqText()
freqDist7.analyseText7()
freqDist7.collocationTxt7()
