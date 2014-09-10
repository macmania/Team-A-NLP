'''
	Temp file to scrape useless noise from Texas */*.txt files

	Vectorizes all of the text files in the Texas folder and performs k-means to better cluster 
	the text to the appropriate feature set. 

	To-do 
'''

import glob
import errno
import nltk
from nltk.collocations import *
import operator
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.probability import FreqDist

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