'''
	Don't touch yet :) 

	extracts the features from the body of text, i.e.: publication format, grammar structure
	then clusters these features based on how similar they are using k-means 

	Solution: 
		Vectorizes all of the text files in the Texas folder -> puts them in a database (in-progress of where to save this)
		Performs k-means to better cluster these features
		
		Look at the cluster and see if there are particular things to look to better perform analysis

		***** Need to write this in Hadoop ******

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

'''
Tags the lines based on their word characteristic: 
	- VB, NNP, etc. 
	- outputs two sets of data structures
		1. a dictionary, removes redudancy 
		2. 
'''
def getTags(text): 
	listTags = []

#Assuming text is a bunch of lines conglomerated together
#lemmatized, lower-cased and amongst other things to sanitize noise in the data
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

