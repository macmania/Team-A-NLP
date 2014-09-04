@@ -0,0 +1,88 @@
from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
from nltk.book import *
from nltk.stem.porter import *



listOfTexts= [text1,text2,text3,text4,text5,text6,text8,text9]

#fdist7= FreqDist(text7)
#fdist7Dict = fdist7.items()

stemmer = PorterStemmer()
processedWords7 = [(stemmer.stem(word).lower()) for word in text7 if word.isalpha()]
fdist7 = FreqDist(processedWords7)

#= [(stemmer.stem(distEntry)).lower() for distEntry in fdist7 if distEntry.isalpha()]

#test = [word for word in fdist7]
#print(test)
#print(fdist7['traffic'])
#print(fdist7['money'])

processedListOfTexts = []
for text in listOfTexts:
    processedWords = [(stemmer.stem(word)).lower() for word in text if word.isalpha()]
    for word in processedWords:
        processedListOfTexts.append(word)


print('appending complete')
setOfProcessedWords = set(processedListOfTexts)
print('creating set complete')
masterDict = {}
dist = FreqDist(processedListOfTexts)
for item in dist.items()[::-1]:
    print(item)

'''
derp = 0
for word in setOfProcessedWords:
    print(derp)
    derp = derp + 1
    masterDict[word] = processedListOfTexts.count(word)

print(masterDict)


fdistMaster = FreqDist(processedListOfTexts)
for distEntry in fdistMaster:
    print(distEntry)


count = 0
masterDict = {}
for text in processedListOfTexts:
    fdist = FreqDist(text)
    print(count)
    count = count+1
    for distEntry in fdist:
        if distEntry in masterDict.keys():
            masterDict[distEntry] = masterDict[distEntry] + fdist[distEntry]
        else:
            masterDict[distEntry] = fdist[distEntry]
'''

sortedDictInAllTxt = dict(sorted(masterDict.items(), key=lambda x: x[1])[:50])


print('herp\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

allWordsIn7Txt = dict(sorted(fdist7.items(), key=operator.itemgetter(1)))

text7DistCommon = {} #the uncommon ones

#get rid of words that are occuring in other text
for common in allWordsIn7Txt:
    #print common, type(common), type(sortedDictInAllTxt)
    if (common not in sortedDictInAllTxt and common in allWordsIn7Txt and 
        allWordsIn7Txt[common] < 1500 and len(common) > 3):
        text7DistCommon[common] = allWordsIn7Txt[common]
     
#needs to be code-proofed
print('\nCollocations')
colloc = text7.collocations();
