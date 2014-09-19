#
import nltk
from nltk.corpus import *
from nltk.probability import *
#from nltk import WhitespaceTokenizer
#from collections import Counter
#inputs:
#outputs:
def createBaseline(sent):
    #baseline=brown.words()
    #baseline=baseline+reuters.words()
    #baseline=baseline+state_union.words()
    #baseline=baseline+nltk.corpus.words.words()#confirm if this exists
##    corpora = ['Brown']
##    cfd = nltk.ConditionalFreqDist(
##... (lang, len(word))
##... for corpus in corpora
##... for word in udhr.words(lang + '-Latin1'))
##    cfd.plot(cumulative=True)
##    cfd = nltk.ConditionalFreqDist(len(word) for word in baseline)
##    fdist=nltk.FreqDist(raw_text)
    
    cfdist = ConditionalFreqDist()
    #words(fileids=[f1,f2,f3])
    corpora = ['Brown', 'Reuters']
    corporaWords=[brown.words(), reuters.words()]
    cfd= nltk.ConditionalFreqDist(
        (corpus,len(word))
        for corpus in corpora
        for word in brown.words() )
    cfd.plot()
text='Hello this is my corpus text. This is good. This is bad.'
createBaseline(text)
