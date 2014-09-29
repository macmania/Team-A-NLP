#!/usr/bin/env python
import sys
import nltk
import cPickle
from cPickle import load

#Import tagger
inp = open('TrigramTagger.pkl', 'rb')
tagger = load(inp)
inp.close()

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

for line in sys.stdin:
    #assume line is the full path for a file
    currentFile = open(line)

    #FOR EACH SENTENCE IN THE FILE
    #   lowercase everything
    #   get POS of all words
    #   lemmatize word??
    #   OUTPUT: word_pos   1   to a file
    sentences = sent_tokenizer.tokenize(currentFile)
    for sent in sentences:
        sent = sent.lower()
        posTagsTuples = tagger.tag(sent)
        for tup in posTagsTuples:
            print '%s\t%s' % (tup[0] + '_' + tup[1], 1)