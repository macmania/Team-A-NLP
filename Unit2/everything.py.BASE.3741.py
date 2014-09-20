import glob
import errno
import nltk
from nltk import FreqDist
import operator
from array import array
import string 
import os

####################################################################
# Scrape useless noise from Texas */*.txt files
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

#analyzes the text based on the number of lines in comparison to the words of a text file
#if there are more lines than text then it's not an article. (Interesting to look at whether a
#   cluster of text may indicate that the text is an article)
#If it's an article then we use a k-means clustering to look at: 
#   - top 10 most frequent words
#   - top collocation phrases   
#If it's not an article then we report:
#   - top 5 most frequent words
#   - find the common phrases
#Question: which one is better? common phrases for an article or most frequent words in 
#                                                                   a non-article
def classifyTxt(strTxt):
    if strTxt == None: 
        print "parameter cannot be empty"
    else:
        numNewLines = 0
        for c in strTxt: 
            if c == '\n':
                numNewLines += 1
        if numNewLines < len(strTxt.split()) and numNewLines != 0:
            return True
        else: 
            return False

#extracts a chunk of text that are similar distance to one another, assuming that the
#article is double or single spaced. 
#returns the extracted text
'''Need to ask Dr. Fox what the best approach would be to classify a particular text: 
    according to the chunk it belongs to, but since for this program we are not classify
    the text on a particular file, we just want to know which content is the most relevant'''
def extractTxtArticle(strTxt):
    strTxt = strTxt.splitlines()
    extractTxt = []
    for r in range(len(strTxt)):
        if len(strTxt[r].strip(' ')) >= 80 and '|' not in strTxt[r] and '#' not in strTxt[r]:
            extractTxt.append(strTxt[r])
    return extractTxt

#Texas folder extraction start
print('Beginning to clean up files and Extraction of article contents')
#files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
files = glob.glob("Islip13Rain/*.txt")
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
extractTxt = ''
stopWords=[]
for name in files: 
    try: 
        with open(name) as f: 
            lines = f.read()
            if classifyTxt(lines):
                artcle += 1 # counts how many articles it has classified successfully
                #if artcle%50==0:
                print ('Articles=',artcle)
                art.append(name)
                fileName=os.path.split(name)[1]
                extractTxt = extractTxtArticle(lines)
                #newFile = open(str("TexasExtractedFiles/" + fileName), 'w')
                newFile = open(str("IslipExtractedFiles/" + fileName), 'w')
                newFile.write(str(extractTxt))
            else:
                stopWords.append(lines)
                nonArtcl += 1
                if nonArtcl%100==0:
                    print('Non article=',nonArtcl)
                nonArt.append(name)
    except IOError as exc: 
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError
print('Extraction of article contents Done')        
####################################################################
#Create stop word lists
# List 1 - MIT's stop word list
print('Starting creation of stop words')
mitStopWords=[]
mitStopWordsFile=open('mit_stop_words.txt')
mitStopWords = [line.strip() for line in mitStopWordsFile]
mitStopWordsFile.close()
# Convert list to hashtable to remove duplicates. Not order preserving.
# List 2 - Our own sublanguage stop word list
keys = {}
for e in stopWords:
   e=str(e).split('\n')
   for element in e:
       if element not in mitStopWords:
           element=str(element).strip()
           keys[element] = 1
stopWordSet= keys.keys()
print('Done creating stop words')
# Write sub-language stop words into file
def writeStopWords(stopWordSet):
    stopWordFile=open('SubLang_StopWords.txt','w')
    for word in stopWordSet:
        stopWordFile.write(str(word))
    stopWordFile.close()
# Write function call
#writeStopWords(stopWordSet)
####################################################################
# listOfTexts contains the raw strings of all cleaned texts
listOfTexts = []
directory = "IslipExtractedFiles/*.txt"
files = glob.glob(directory)
print('There were '+str(len(files))+' files found in the ' + directory + ' directory.')
for curr in files:
    try:
        with open(curr) as f:
            raw = f.read()
            listOfTexts.append(raw)
    except IOError as e:
        if e.errno != errno.EISDIR:
            raise
print('\nListOfTexts has: '+str(len(listOfTexts))+' texts in it')
####################################################################
# Process the raw strings
print('\nStarting lemmatizing, normalization and removal of stop-words')
wnl = nltk.WordNetLemmatizer()
processedListOfTexts = []
nounList=[]
for text in listOfTexts:
    #temp=[]
    wordsInText=text.split()
    for i in range(0,len(wordsInText)-1):
        word=wordsInText[i]           
        if wordsInText[i-1]!='.' and word.istitle(): # Look for capital first letter for nouns. Nouns are of special interest to us.    
            nounList.append(word.lower())
        # Stemming and normalization
        lemWord=(wnl.lemmatize(word)).lower()
        if lemWord not in mitStopWords and word.isalpha(): # beware : we lose number info    
            processedListOfTexts.append(lemWord) # append all processed words in a particular text to masterList         
print('Done lemmatizing and normalization')
####################################################################
# Hash the nounList
print('Hashing the nounList')
keys={}
for noun in nounList:
    if noun not in stopWordSet:
        #print(noun)
        keys[noun]=1
nounList=keys.keys()
####################################################################
#FreqDist
#requires tokenized nltk/string. Also can use ' '.join(processedListOfTexts)
print('\n--------------------------------------------------\nCompute most frequent indicative words')
fullDist = FreqDist(str(word) for word in processedListOfTexts)
#Use items() because most_common() doesn't work on mac.
#Note: Please confirm if output of items() is sorted by value
top=[word[0] for word in fullDist.items()[:150] if word[0] not in stopWordSet and (len(word[0])<15 or word in nounList)]
for word in top:
    if word.isalpha():
        print(word)
probable=[]
print('\n--------------------------------------------------\nProbable words:')
for word in top:
    if word in nounList:
        probable.append(word)
        print(word)
print('\n--------------------------------------------------\nCollocations throughout all texts: ')
#processedListofText
