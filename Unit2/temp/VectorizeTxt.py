'''
	Don't touch yet :) 

	extracts the features from the body of text, i.e.: publication format, grammar structure
	then clusters these features based on how similar they are

	Vectorizes all of the text files in the Texas folder and performs k-means to better cluster 
	the text to the appropriate feature set. 

	Lots of to-do
 						-----In progress-----
'''

import glob
import errno
import nltk
from nltk.collocations import *
import operator
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.probability import FreqDist
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


def extractFeatures(text): 
	#to-do
	print 'hello'
	return True

def getTags(text): 
	listTags = []

#Assuming text is a bunch of lines conglomerated together
def filter(allText): 
	if allText == None: 
		return
	filteredText, words, tokens = [], [], []
	for lines in allText: 
		tokens = word_tokenize[lines]



def readFiles() : 
	#Texas folder collocation start
	files = glob.glob("../Islip13Rain/*.txt")
	artcle, nonArtcl = 0, 0
	art, nonArt = [], [] 
	extractTxt = ' '
	stemmer = PorterStemmer()
	stops = set(stopwords.words('english'))
	for name in files: 
		try: 
			with open(name) as f: 
				lines = f.read().split()
				lines = [word.lower() for word in lines if word.lower() not in stops and len(word) > 2]
				lines = [(stemmer.stem(w).lower()) for w in lines if len(w) > 2]
				x = FreqDist(lines)
				for l in x: 
					print l, x[l]
		except IOError as exc: 
			if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
				raise # Propagate other kinds of IOError.

