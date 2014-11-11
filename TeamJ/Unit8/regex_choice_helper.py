import glob, os, re

small_NEs_loc = set(['newtown', 'connecticut', 'sandy hook elementary school'])
small_NEs_person = set(['Adam Lanza'])
#small_words=set(['shooting', 'victims', 'gunman', 'school', 'children', 'students', 'police', 'dead','wounded', 'weapon', 'firearm', 'motive'])

files = glob.glob('../collections/SmallCollParas/*.txt')
for fileName in files:
    f= open(fileName)
	f1= open('location_sentences.txt')
    fullText= f.read().lower()
    sents= fullText.split('.')
	for sent in sents:
		if any(word in small_NEs_loc for word in wordsInPara):
			f1.write(sent)
	f1.close()
    f.close()            
        
    
