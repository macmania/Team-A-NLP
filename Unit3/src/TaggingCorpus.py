'''
	Separates the text in ClassEvent sentences and tags them in the appropriate
  manner.
'''
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
import sys, os





#a text of body that needs to
def tag(text):
  if text == "":
    return


######################sets up the path######
currPath = os.path.abspath("")
startPath = 0
endPath = len(currPath) - 1
pathSrc = currPath[0:endPath-9] + '/lib/src/'
pathClass = currPath[0:endPath-9] + '/lib/ClassCode/'
sys.path.append(pathSrc)
sys.path.append(pathClass)
from FilterFiles import extractTxtArticle
##########################################

CEcorpus_root = '../../lib/Corpus/ClassEvent'
CEWordLists = PlaintextCorpusReader(CEcorpus_root, ".*\.txt")
CE = CEWordLists.raw()
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
extractTxt = extractTxtArticle(CE)
CE = "".join(extractTxt)
CEsents = sent_tokenizer.tokenize(CE)


print 'ClassEvent Sentence tokens: ', (CEsents[1:10])
