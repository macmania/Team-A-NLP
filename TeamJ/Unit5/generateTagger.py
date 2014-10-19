from __future__ import division
import nltk
import os
from nltk.tag.stanford import NERTagger
import pickle
st = NERTagger('/home/peter/Documents/school/Team-A-NLP/TeamJ/standfordNER/classifiers/english.all.3class.distsim.crf.ser.gz', '/home/peter/Documents/school/Team-A-NLP/TeamJ/standfordNER/stanford-ner.jar') 
pickle.dump(st, open('stanfordNER.pickle', 'wb'))