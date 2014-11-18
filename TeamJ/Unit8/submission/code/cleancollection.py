# -*- coding: utf-8 -*-
import os, glob, sys, codecs
from cPickle import *
import zipimport
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]
input = open('tokenizer.pkl','rb')
sent_tokenizer= load(input)

stopfile = open('customstop.txt', 'r')
some_stops = stopfile.readlines()

print sys.argv[1]
print sys.argv[2]

files = glob.glob(sys.argv[1]+'/*');
for filename in files:
	print filename
	try:
		fileObj= codecs.open(filename, 'r', 'utf-8')
    		text= fileObj.read()
	except:
		continue
    	sents = sent_tokenizer.tokenize(text)
	name = os.path.basename(filename);
	outsents = []
	for sent in sents:
		words = map(lambda x: x.lower(), sent.split(' '));
		add = True
		for word in words:
			if word in some_stops:
				add = False
				break
			if len(word) > 16:
				add = False
				break
		if add:
			outsents.append(sent)
	if len(outsents) > 0:
		with codecs.open(sys.argv[2] + name, 'w', 'utf-8') as newfile:
			#print name
			#print sys.argv[2] + name + ".txt"
			for l in outsents:
				newfile.write(l)
	else:
		print "no output"
