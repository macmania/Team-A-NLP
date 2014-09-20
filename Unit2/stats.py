#import __future__
import nltk
from nltk import tokenize
from decimal import *
#from __future__ import division

# inputs: 1) fullText, 2) stop-word list(ours/mit's) 3)
# outputs: 1)
#global:

def stats(listOfTexts, stopList, YourWords):
    totalWords=0
    totalLetters=0
    totalSentences=0
    countNotInStop= 0
    countInRange1_15= 0

    YourWordsDict = {}

#    for line in fullTextInLines:

    print("ENTERING STATS")
    for text in listOfTexts:
        #print("THE TEXT IS:")
        #print(text)
        fullTextInLines = nltk.sent_tokenize(text)

        #print("THE TOKENIZED TEXT IS")
        #print(fullTextInLines)
        for line in fullTextInLines:
            totalSentences = totalSentences + 1
            for word in line.split():
                # to find average number of letters per word
                totalLetters = totalLetters + len(word) 
                totalWords = totalWords + 1
                if word in YourWords:
                    if word in YourWordsDict.keys():
                        YourWordsDict[word] = YourWordsDict[word] + 1
                    else:
                        YourWordsDict[word] = 1
                # to find percent of words less than 15 letters in length
                if len(word)<16:
                    countInRange1_15 = countInRange1_15 + 1
                if word not in stopList:
                    countNotInStop = countNotInStop + 1


    print(totalSentences)
    print(totalWords)
    print(totalLetters)
    print(countNotInStop)
    print(countInRange1_15)

    averageLettersPerWord= Decimal(totalLetters)/Decimal(totalWords)
    percentWordsNotInStop= (Decimal(countNotInStop)/Decimal(totalWords))*100
    percentWordsInRange1_15=(Decimal(countInRange1_15)/Decimal(totalWords))*100
    averageWordsPerSentence= Decimal(totalWords)/Decimal(totalSentences)
    
    print('averageLettersPerWord ', averageLettersPerWord)
    print('percentWordsNotInStop', percentWordsNotInStop)
    print('percentWordsInRange1_15', percentWordsInRange1_15)
    print('averageWordsPerSentence', averageWordsPerSentence)
    # % of occrrence of each word in YourWords stored as value in YourWordsDicy
    for word in YourWords:
        YourWordsDict[word]=YourWordsDict[word]/totalWords
    # 4.71 uw + 0.5 us - 21.43
    ARI= 4.71*averageLettersPerWord + 0.5*averageWordsPerSentence  - 21.43