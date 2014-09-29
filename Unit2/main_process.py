from nltk import FreqDist
import noiseFilter_1
import noiseFilter_2 
from stopWordLists import *
from cleanUp import *
from normalize import *

#Global variables
extractTxt = ''
sublStopWords=[]
stopWordSet=[]
mitStopWords=[]
processedListOfTexts = []
nounList=[]
    
def processTexts(processedListOfTexts):
    #FreqDist
    print('\n--------------------------------------------------\nCompute most frequent indicative words')
    #requires tokenized nltk/string. Also can use ' '.join(processedListOfTexts)
    fullDist = FreqDist(str(word) for word in processedListOfTexts)
    #Use items() because most_common() doesn't work on mac.
    #Note: Please confirm if output of items() is sorted by value
    top=[word[0] for word in fullDist.most_common(50) if word[0] not in stopWordSet]
    for word in top:
        print(word)
    relevantNouns=[]
    print('\n--------------------------------------------------\nRelevant Nouns:')
    for word in top:
        if word in nounList:
            relevantNouns.append(word)
            print(word)

    #print('\n--------------------------------------------------\nCollocations throughout all texts: ')

def main():
    mitStopWords = createMitStopWordList() # New is in mit stopword list! NEW York!
    #cleanUp_1(extractTxt,sublStopWords)
    cleanUp_2(extractTxt)
    normalize(processedListOfTexts,mitStopWords,nounList)
    processTexts(processedListOfTexts)

if __name__ == "__main__":
    main()
