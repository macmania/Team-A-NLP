'''
	Separates the text in ClassEvent sentences and tags them in the appropriate
  manner.
'''
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
import sys




#a text of body that needs to
def tag(text):
  if text == "":
    return



currPath = os.path.abspath("")
startPath = len(currPath) - 19
endPath = len(currPath) - 1
path = currPath[startPath:endPath]

sys.path.append("../")
CEcorpus_root = '../../lib/Corpus/ClassEvent'

CEWordLists = PlaintextCorpusReader(CEcorpus_root, ".*\.txt")
CE = CEWordLists.raw()
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
CEsents = sent_tokenizer.tokenize(CE)

print 'ClassEvent Sentence tokens: ', (CEsents)
print 'ClassEvent Sentence tokens: '
print "\n".join(CEsents)




print 'ClassEvent Sentence tokens: ', (CEsents[1:10])
