'''
	Filters the file based on the structure, still a lot to do to improve
	the criterion on removing the noise
'''
import nltk
import re

#input : rawText Before tokenization.
#output: Input raw text is split into sentences. Non-sentences are discarded.
def noiseFilter_2(rawText):
    rawSentences=re.findall( '.+?[.?!]',rawText)
    sentences= [sent for sent in rawSentences if len(sent)>80]
    return sentences


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

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

def extractTxtArticle(strTxt):
		strTxt = strTxt.splitlines()
		extractTxt = []
		for r in range(len(strTxt)):
		  if len(strTxt[r].strip(' ')) >= 80 and '|' not in strTxt[r] and '#' not in strTxt[r]:
		      if (is_ascii(strTxt[r])):
		          extractTxt.append(strTxt[r])
		return extractTxt

def createStopWordsCollection():
	mitStopWords=[]
	mitStopWordsFile=open('../../lib/StopWords/mit_stop_words.txt')
	mitStopWords = [line.strip() for line in mitStopWordsFile]
	mitStopWordsFile.close()
	return mitStopWords


def removeStopWords(text):
	mitStopWords = createStopWordsCollection()
	keys = {}
	for e in text:
		e=str(e).split('\n')
		for element in e:
				if element not in mitStopWords:
						element=str(element).strip()
						keys[element] = 1
	stopWordSet= keys.keys()
	return stopWordSet


# Write sub-language stop words into file
def writeStopWordsFile(stopWordSet, fileName):
		stopWordFile=open('../output/' + fileName,'w')
		for word in stopWordSet:
				stopWordFile.write(str(word))
		stopWordFile.close()
