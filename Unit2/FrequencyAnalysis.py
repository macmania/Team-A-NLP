from __future__ import division
from nltk.probability import FreqDist
from nltk import FreqDist
import nltk
import operator
#from nltk.book import *
from nltk.stem.porter import *
import glob


print('Starting creation of stop words')

stopWords = []
mitStopWordsFile = open('mit_stop_words.txt')
stopWords = [line.strip() for line in mitStopWordsFile]
mitStopWordsFile.close()

print('Done creating stop words')


#Populate the list of texts to be used
listOfTexts = []
directory = "TexasExtractedFiles/*.txt"
files = glob.glob(directory)
print('There were ')
print(len(files))
print('files found in the ' + directory + ' directory.')

#count = 0
for curr in files:
#	count = count + 1
#	if (count % 50) == 0:
#		print(count)

	try:
		with open(curr) as f:
			raw = f.read()
			#TOKENIZE??????????????????
			tokens = nltk.word_tokenize(raw)
			text = nltk.Text(tokens)
			listOfTexts.append(text)

	except IOError as e:
		if e.errno != errno.EISDIR:
			raise


print('listOfTexts has: ')
print(len(listOfTexts))
print('texts in it')


#Process texts
print('starting stemming and processing')

stemmer = PorterStemmer()
processedListOfTexts = []
for text in listOfTexts:
    processedWords = [(stemmer.stem(word)).lower() for word in text if word.isalpha()]
    for word in processedWords:
        processedListOfTexts.append(word)

print('Done stemming and stuff')



fullDist = FreqDist(processedListOfTexts)
#Use items() because most_common() doesn't work on mac
for word in fullDist.items()[:75]:
    if word[0] not in stopWords:
    	print(word[0])

