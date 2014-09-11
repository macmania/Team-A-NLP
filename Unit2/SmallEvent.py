'''
	Temp file to scrape useless noise from Texas */*.txt files
'''

import glob
import errno
import nltk
from nltk import FreqDist
from nltk.collocations import *
import operator
<<<<<<< HEAD
=======
from array import array
import string 

def is_ascii(s):
	'''if s == '\'': 
		return False '''

	return all(ord(c) < 128 for c in s)
>>>>>>> FETCH_HEAD

#analyzes the text based on the number of lines in comparison to the words of a text file
#if there are more lines than text then it's not an article. (Interesting to look at whether a
#	cluster of text may indicate that the text is an article)
#If it's an article then we use a k-means clustering to look at: 
#	- top 10 most frequent words
#	- top collocation phrases	
#If it's not an article then we report:
#	- top 5 most frequent words
#	- find the common phrases
#Question: which one is better? common phrases for an article or most frequent words in 
#																	a non-article
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
<<<<<<< HEAD
			extractTxt.append(strTxt[r])

	#print extractTxt
	return extractTxt



=======
			strTxt[r] = [s for s in strTxt[r].strip(' ') if is_ascii(s)]
			extractTxt.append("".join(strTxt[r]).replace("\t", ""))

	return extractTxt

>>>>>>> FETCH_HEAD
#Texas folder collocation start
files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
artcle, nonArtcl = 0, 0
art, nonArt = [], [] 
extractTxt = ' '
numArticles = 0
for name in files: 
	try: 
		with open(name) as f: 
			lines = f.read()
			if classifyTxt(lines):
				artcle += 1
				art.append(name)
				extractTxt = extractTxtArticle(lines)
<<<<<<< HEAD
				print name[33:]
				newFile = open(str("TexasExtractedFiles/" + name[33:]), 'w')
				newFile.write(str(extractTxt))
				numArticles += 1
				#print extractTxt
=======
				newFile = open(str("TexasExtractedFiles/" + name[33:]), 'w')
				newFile.write(str(extractTxt))
				#numArticles += 1, counts how many articles it has classified successfully
>>>>>>> FETCH_HEAD
	
			else: 
				extractTxt = lines.split()
				nonArtcl += 1
				nonArt.append(name)
<<<<<<< HEAD

	except IOError as exc: 
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.

print numArticles
=======
		extractTxt = ' '
	except IOError as exc: 
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.
>>>>>>> FETCH_HEAD
