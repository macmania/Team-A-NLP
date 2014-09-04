from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
from nltk.book import *
#from nltk.book import text1 - find a way to do this
'''
import dateutil
import pyparsing
import numpy
import six
import matplotlib
'''
listOfTexts= [text1,text2,text3,text4,text5,text6]
fdist1= nltk.FreqDist(text7)
commonWords=fdist1.items() #????
#fdist1.plot(50, cumulative=False)
indicativeWords= [word[0] for word in commonWords if word[0].isalpha()]
#if len(word[0])>4 ]
count = 0
masterDict = {}
for text in listOfTexts:
    fdist = FreqDist(text)
    count = count+1
    #print(count)
    for word in fdist:
        if word in masterDict.keys():
            masterDict[word] = masterDict[word] + fdist[word]
        else:
            masterDict[word] =fdist[word]

sortedDictInAllTxt = dict(sorted(masterDict.items(), key=lambda x: x[1]))


'''for herp in sortedDict:
    print(herp)'''


print('herp\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

text7Dist = FreqDist(text7)
allWordsIn7Txt = dict(sorted(text7Dist.items(), key=operator.itemgetter(1))[:50])
#commonWords = {k:v for k, v in commonWords.items() if v > 10}
#find the 100th elements

#retrieve top 50 words that appears in other texts(some arbitrary)
#allWordsIn7Txt = allWordsIn7Txt[:50]
text7DistCommon = {} #the uncommon ones

#get rid of words that are occuring in other text
for common in allWordsIn7Txt:
    print common, type(common), type(sortedDictInAllTxt)
    if (common not in sortedDictInAllTxt and common in allWordsIn7Txt and 
        allWordsIn7Txt[common] < 1500):
        text7DistCommon[common] = allWordsIn7Txt[common]

print text7DistCommon        
        

#print(sorted(masterDict.items(), key=lambda x: x[1]))
 
print('\nCollocations')
colloc= text1.collocations();

#To count percentage of occurrence of each of the words...
#wordPercentList= List of % of usage
wordPercentList, textLength = [], len(text1)

print (len(indicativeWords))

#Implement stop word filters
ignored_words = (open('nltk_english_stopWords.txt')).read().split()
for word in indicativeWords:
    if word in ignored_words:
        print (word, ' found and removed')
        indicativeWords.remove(word)

# word Is indeed indicative
for word in indicativeWords:    
    wordPercentList.append(100*text1.count(word)/textLength)
print (len(indicativeWords)), (len(wordPercentList))


print('\nPercentage list of all indicative words:\n')
for i in range(0,len(indicativeWords)-1):
    print(indicativeWords[i],wordPercentList[i])