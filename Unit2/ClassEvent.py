'''
	Extracts the appropriate corpus characteristics of the classevent text 
'''

from nltk.corpus import PlaintextCorpusReader

corpus_root = 'Islip13Rain'
worldlists = PlaintextCorpusReader(corpus_root, '.*')
print worldlists.fileids()
