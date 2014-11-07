import os, glob, sys
from cPickle import *
import zipimport
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]
input = open('tokenizer.pkl','rb')
sent_tokenizer= load(input)

stopfile = open('customstop.txt', 'r')
some_stops = stopfile.readlines()

count = 0

files= glob.glob('collections/POSITIVECleanBigCollectionFiles/*.txt')
for filename in files:
    fileObj= open(filename)
    text= fileObj.read()
    sents = sent_tokenizer.tokenize(text)  # sents= list of sentences(strings)
    name= os.path.basename(filename) # name without extension
    sentCount=1
    for sent in sents:
	words = map(lambda x: x.lower(), sent.split(' '))
	if(len(words) < 4):
		continue
	stop = False
	for word in words:
		if word in some_stops:
			stop = True
			break;
		if len(word) > 16:
			stop = True
			break;
	if stop:
		continue
        newFile= open('collections/BigEventAsSents/'+name[:-4]+'_'+str(sentCount)+'.txt','w')        
	#sent_utf= sent.encode(encoding='UTF-8',errors='ignore')
	sent_utf= sent
        sentCount+=1
	if sentCount %20 == 0:
        	print 'writing '+ name[:-4]+'_'+str(sentCount)
        #print sent+ ' gave (unicode?) error'
	newFile.write(sent_utf)
        newFile.close()
        count += 1
	if count >= 15000:
		break;
    if count >= 15000:
	break;
