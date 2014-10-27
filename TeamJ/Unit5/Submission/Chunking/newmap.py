#!/usr/bin/env python
import sys
import nltk
import cPickle
from cPickle import load
from nltk.tree import Tree
reload(sys)
sys.setdefaultencoding('utf-8')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

for line in sys.stdin:
    #assume line is the full path for a file
    currentFile = open(line.rstrip())
    fullFile=currentFile.read()
    sentences = sent_tokenizer.tokenize(fullFile) #sentences = list of sentence strings
    for sent in sentences: # each sentence in file
        try :
	    tokens = nltk.word_tokenize(sent) # tokens= list of tokens in a sentence
            tags = nltk.pos_tag(tokens) # tags = list of tuples (token/word, tag)
            chunk= nltk.ne_chunk(tags, binary=False)
            if isinstance(chunk,Tree):
                #print len(chunk)
                for node in chunk :
		    for node in chunk :
                    	if isinstance(node,Tree):
                    	    print '%s\t%s' % (str(node), 1)
        except:
            print 'Error'

