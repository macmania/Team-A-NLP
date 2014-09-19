# inputs: 1) fullText, 2) stop-word list(ours/mit's) 3)
# outputs: 1)
#global:

def stats(fullTextInLines, stopList, YourWordsDict):
    totalWords=0
    totalLetters=0
    totalSentences=0
    countNotInStop= 0
    countInRange1_15= 0
    for line in fullTextInLines:
        totalSentences+=1
        for word in line:
            # to find average number of letters per word
            totalLetters+= len(word) 
            totalWords+=1
            if word in YourWordsDict.keys():
                YourWordsDict[word]+=1
            # to find percent of words less than 15 letters in length
            if len(word)<16:
                countInRange1_15+=1
            if word not in stopList:
                countNotInStop+=1
    averageLettersPerWord= totalLetters/totalWords
    percentWordsNotInStop= (countNotInStop/lenFullText)*100
    percentWordsInRange1_15=(countInRange1_15/lenFullText)*100
    averageWordsPerSentence= totalWords/totalSentences
    # % of occrrence of each word in YourWords stored as value in YourWordsDicy
    for word in YourWordsDict.keys():
        YourWordsDict[word]=YourWordsDict[word]/totalWords
    # 4.71 uw + 0.5 us - 21.43
    ARI= 4.71*averageLettersPerWord + 0.5*averageWordsPerSentence  - 21.43
