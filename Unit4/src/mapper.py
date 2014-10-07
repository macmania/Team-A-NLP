#!/usr/bin/env python
import sys
import nltk
import cPickle
from cPickle import load
import re

#import featureList
input= open('featureList.pkl','rb')
featureList= load(input)
input.close()
# import best classifier model
input = open('classifierModel.pkl', 'rb')
classifier = load(input)
input.close() 
# input is file with fullpath filenames
for line in sys.stdin:
    #assume line is the full path for a file
    currentFile = open(line[:-1])
    #extract features
    text= currentFile.read()
    featureset={}
    for word in featureList:
        if re.search(word, text):
            featureset[word]= True
        else:
            featureset[word]= False        
    print line[:-1]+'\t'+ classifier.classify(featureset)
    
    


    
