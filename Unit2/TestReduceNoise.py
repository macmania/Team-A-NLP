'''
    Tests whether reducing the noise have improved our analysis. 
    We compare the results between the results that has been pre-reduced noise
    and one that hasn't reduced noise. 
'''
import glob
import errno
import nltk
from nltk import FreqDist
import operator
from array import array
import string 
import os
import subprocess

# Write sub-language stop words into file
def writeStopWords(stopWordSet):
    stopWordFile=open('SubLang_StopWords.txt','w')
    for word in stopWordSet:
        stopWordFile.write(str(word))
    stopWordFile.close()

#Texas folder extraction start
print('Beginning to clean up files and Extraction of article contents')
#files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
files = glob.glob("Islip13Rain/*.txt")
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
extractTxt = ''
stopWords=[]
   
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

listOfTexts = []
files = glob.glob("Islip13Rain/*.txt")

for curr in files:
    try:
        with open(curr) as f:
            raw = f.read()
            listOfTexts.append(raw)
    except IOError as e:
        if e.errno != errno.EISDIR:
            raise

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

keys={}
for noun in nounList:
    if noun not in stopWordSet:
        keys[noun]=1
nounList=keys.keys()


print('\n--------------------------------------------------\nCompute most frequent indicative words')
fullDist = FreqDist(str(word) for word in processedListOfTexts)
wordsWithNoise = []
#Note: Please confirm if output of items() is sorted by value
top=[word[0] for word in fullDist.items()[:150] if word[0] not in stopWordSet and (len(word[0])<15 or word in nounList)]
for word in top:
    if word.isalpha():
        wordsWithNoise.append(word)

p = subprocess.Popen(["python", "everything.py"], stdout=subprocess.PIPE)
output, err = p.communicate() 
x = output.splitlines()
wordsWithOutNoise = [] 
start, end, l = 0, 0,0
for words in x: 
    l += 1
    if words == 'Compute most frequent indicative words':
        start = l
    if words =="Probable words:":
        end = l
wordsWithOutNoise = x[start:end-3]

print [(w, wordsWithOutNoise.count(w)) for w in set(wordsWithOutNoise) if w in wordsWithNoise]

for x in range(len(wordsWithOutNoise)):
    print wordsWithNoise[x], wordsWithOutNoise[x]
        




