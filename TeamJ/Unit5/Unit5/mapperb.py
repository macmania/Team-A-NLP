#!/usr/bin/env python

import sys
import cPickle
from cPickle import load
import re
import zipimport
import os

reload(sys)
sys.setdefaultencoding('utf-8')

pathtojava = "/usr/bin/java";
#os.environ['JAVAHOME'] = pathtojava

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.internals.config_java(pathtojava);
nltk.data.path += ["./nltkData/"]

from nltk.tag.stanford import NERTagger
nltk.internals.config_java(pathtojava);
#stanfordTagger = NERTagger('english.all.3class.distsim.crf.ser.gz', 'stanford-ner.jar', 'utf-8')

input = open('stanfordNER.pickle', 'rb')
stanfordTagger = load(input);
input.close()

# input is file with fullpath filenames
for line in sys.stdin:
	text = line
	if len(text) > 0 and text != None:	
    		#print text.split();
		for t in stanfordTagger.tag(text.split()):
			if len(t[0]) > 2 and t[1] != 'O':
				print '%s_%s\t%d' % (t[1], t[0].lower(), 1)
