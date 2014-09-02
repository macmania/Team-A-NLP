from __future__ import division
import nltk
from nltk.book import *
#from nltk.book import text1 - find a way to do this
import dateutil
import pyparsing
import numpy
import six
import matplotlib

fdist1= FreqDist(text1)
commonWords=fdist1.most_common(500) #????
#fdist1.plot(50, cumulative=False)
indicativeWords= [word[0] for word in commonWords if len(word[0])>4 ]
#print (len(indicativeWords),' most common words with frequency: \n',indicativeWords)
print('\nCollocations')
colloc= text1.collocations();

#To count percentage of occurrence of each of the words...
#wordPercentList= List of % of usage
textLength= len(text1)
wordPercentList=[]
for word in indicativeWords:
    wordPercentList.append(100*text1.count(word)/textLength)

print('\n',type(indicativeWords))
print('\nPercentage list of all indicative words:\n')
for i in range(0,len(indicativeWords)-1):
    print(indicativeWords[i],'\t',wordPercentList[i])
    
    