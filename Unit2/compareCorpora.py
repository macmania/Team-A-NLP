#
import nltk
from nltk.corpus import *
from nltk.probability import *
#from nltk import WhitespaceTokenizer
#from collections import Counter
#inputs:
#outputs:
def createBaseline(YourWords):
    #fullText = brown.raw() + reuters.raw() + state_union.raw() + nltk.corpus.words.raw()
    #f = open('ALLRAW.txt', 'w')
    #f.write(fullText)
    #f.close()

    f = open('ALLRAW.txt')
    fullText = f.read()
    f.close()
    print(len(fullText))

    '''
    baseline=brown.words()
    baseline=baseline.append(reuters.words())
    baseline=baseline.append(state_union.words())
    baseline=baseline.append(nltk.corpus.words.words())#confirm if this exists
    '''
    baselineFdist=FreqDist(nltk.Text(fullText))

    f = open('ISLIPPROCESSED.txt')
    classEvent= nltk.Text(f.read().lower().split()) #???
    classEventFdist=FreqDist(classEvent)
    f.close()

    f = open('TEXASPROCESSED.txt')
    texasEvent= nltk.Text(f.read().lower().split())
    texasEventFdist=FreqDist(texasEvent)
    f.close()

    print(baselineFdist)
    print(classEventFdist)
    print(texasEventFdist)

    cfdist = ConditionalFreqDist()
##    #words(fileids=[f1,f2,f3])
    corporaDist=[classEventFdist, texasEventFdist, baselineFdist]
    for word in str(YourWords).split():
        word = '\''+word+'\''
        baseVal=baselineFdist[word]
        classVal=classEventFdist[word]
        texasVal = texasEventFdist[word] 
        print('word: ', word, ' classVal: ', classVal, ' baseVal: ', baseVal, ' texasVal: ', texasVal)

    cfdist = ConditionalFreqDist()
    #words(fileids=[f1,f2,f3])
    #corpora = ['Brown', 'Reuters', 'Word List Corpora']
    corporaList =[brown, reuters, words, state_union]
    
    cfd= nltk.ConditionalFreqDist(
        (corpora, len(word))
        #for corpus in corpora
        for corpora in corporaList
        for word in corpora.words() )
    cfd.plot()
    
#text= 'rain water long island islip wednesday state road town august weather york county flood flash storm damage suffolk service parkway'
text = 'people fertilizer plant explosion texas west april boston news find fire time point volunteer blast state town community marathon suspect'
createBaseline(text)
