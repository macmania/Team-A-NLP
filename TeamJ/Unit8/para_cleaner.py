import glob, os

#class_NEs=set(['new york','islip', ' suffolk ', 'long island'])
#class_words= set(['rain', 'raining', 'water', 'inches', 'record', 'wednesday', 'weather', 'flood', 'damage', 'storm' ])
small_NEs = set(['newtown', 'connecticut', 'sandy hook elementary school', 'Adam Lanza'])
small_words=set(['shooting', 'victims', 'gunman', 'school', 'children', 'students', 'police', 'dead','wounded', 'weapon', 'firearm', 'motive'])

files = glob.glob('../lib/ClassEvent/*.txt')
for fileName in files:
    f= open(fileName)
    name= os.path.basename(fileName)
    f1= open('../lib/ClassEventParas/'+name, 'w')
    fullText= f.read().lower()
    paras= fullText.split('\n')
    for para in paras:
        wordsInPara= para.split()
        if any(word in small_NEs for word in wordsInPara):
            if any(word in small_words for word in wordsInPara):
                f1.write(para)

    f1.close()
    f.close()            
        
    
