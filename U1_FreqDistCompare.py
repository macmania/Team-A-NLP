from __future__ import division
import nltk
from nltk.book import *
#from nltk.book import text1 - find a way to do this
import dateutil
import pyparsing
import numpy
import six
import matplotlib

listOfTexts= [text1,text2,text3,text4,text5,text6]
fdist1= FreqDist(text7)
commonWords=fdist1.most_common(100) #????
#fdist1.plot(50, cumulative=False)
indicativeWords= [word[0] for word in commonWords if word[0].isalpha()]
#if len(word[0])>4 ]
count= 0
masterDict = {}
for text in listOftext:
    fdist = FreqDist(text)
    count= count+1
    print(count)
    for word in fdist:
        if word in masterDict.keys():
            masterDict[word] = masterDict[word] + fdist[word]
        else:
            masterDict[word] =fdist[word]
 
print('\nCollocations')
colloc= text1.collocations();

#To count percentage of occurrence of each of the words...
#wordPercentList= List of % of usage
textLength= len(text1)
wordPercentList=[]
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
print (len(indicativeWords))
print (len(wordPercentList))
#print('\n',type(indicativeWords))
print('\nPercentage list of all indicative words:\n')
for i in range(0,len(indicativeWords)-1):
    print(indicativeWords[i],wordPercentList[i])
      
