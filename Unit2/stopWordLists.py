#-------------------------------------------------------------------------------------------------------------
# input: mit stop word list file
# output: mitStopWordList
def createMitStopWordList():
    # List 1 - MIT's stop word list
    print('Starting creation of stop words')
    mitStopWordsFile=open('mit_stop_words.txt')
    mitStopWords = [line.strip() for line in mitStopWordsFile]
    mitStopWordsFile.close()
    return mitStopWords
#-------------------------------------------------------------------------------------------------------------
# input: sublStopWordList set (unique list of sublStopWords)
# output: file containing set of sub-language stop words
def writeStopWords(stopWordSet):
    stopWordFile=open('SubLang_StopWords.txt','w')
    for word in stopWordSet:
        stopWordFile.write(str(word))
    stopWordFile.close()

#-------------------------------------------------------------------------------------------------------------
# input: sublStopWordList set (unique list of sublStopWords)
# output: file containing set of sub-language stop words   
def createSublStopWordList(stopWordSet):
    # Convert list to hashtable to remove duplicates. Not order preserving.
    keys = {}
    for e in sublStopWords:
       e=str(e).split('\n')
       for element in e:
           if element not in mitStopWords:
               element=str(element).strip()
               keys[element] = 1
    stopWordSet= keys.keys()
    print('Done creating stop words')
    #writeStopWords(stopWordSet)

#-------------------------------------------------------------------------------------------------------------
# input: 
# output: 
# Hash the nounList
##print('Hashing the nounList')
##keys={}
##for noun in nounList:
##    if noun not in stopWordSet:
##        #print(noun)
##        keys[noun]=1
##nounList=keys.keys()
####################################################################
