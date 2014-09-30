#!/usr/bin/env python
import sys
import nltk
import cPickle
from cPickle import load

# import punkt tokenizer
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#Import tagger 
inp = open('/home/cla/UITeamA/Unit3/src/TrigramTagger.pkl', 'rb')
tagger = load(inp)
inp.close()
# import lemmatizer
wnl = nltk.WordNetLemmatizer()

for line in sys.stdin:
    #assume line is the full path for a file
    currentFile = open(line)
    fullFile=currentFile.read()
    print fullFile
    #FOR EACH SENTENCE IN THE FILE
    #   lowercase everything
    #   get POS of all words
    #   lemmatize word??
    #   OUTPUT: word_pos   1   to a file
    sentences = sent_tokenizer.tokenize(fullFile) #sentences = list of sentence strings
    print sentences
    for sent in sentences: # each sentence in file
        sent = sent.lower()
        posTagsTuples = tagger.tag(sent) # use Trigram tagger to tag sentence
        for tup in posTagsTuples:
            print tup
            lemmatizedWord = wnl.lemmatize(tup[0])
            print '%s\t%s' % (lemmatizedWord + '_' + tup[1], 1)


    