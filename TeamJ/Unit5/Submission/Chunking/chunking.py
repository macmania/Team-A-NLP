import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tree import Tree
from nltk.probability import FreqDist

#Store appropriate path for corpus we are using
#classEventPath='../Team-A-NLP/lib/Corpus/IslipExtractedFiles'
smallEventPath='../CollectionSmall'
cleanedFilesPath=smallEventPath
# obtain stringized version of corpus
allTexts= PlaintextCorpusReader(cleanedFilesPath, ".*\.txt")
stringOfTexts = allTexts.raw() # read all texts, stringOfTexts = string of all texts
print 'Done creating string of all texts'

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(stringOfTexts) # sents= list of sentences(strings)
print 'Total Tokenized sentences: '+ str(len(sents))
f=open('smallEvent_NEs.txt','w')

#--------------------------------------------------------------
# Question 2.1 and 2.2
def ner_chunk(sents):
    ''' NE Recognition and experimenting with each type of entity'''
    #listAllChunks,listNe, listOfTags= [],[],[]
    count=0
    for sent in sents:        
	print (count)
        count+=1
	tokens = nltk.word_tokenize(sent) # tokens= list of tokens in a sentence
        tags = nltk.pos_tag(tokens) # tags = list of tuples (token/word, tag)
        chunk= nltk.ne_chunk(tags, binary=False)
        if isinstance(chunk,Tree):
            #print len(chunk)
            for node in chunk :
                if isinstance(node,Tree):
                    #print str(node)
                    f.write(str(node)+'\n')
    f.close()
#--------------------------------------------------------------
def experiments():
    f = open('classEvent_NEs.txt','r')
    # Displaying top occurring K NEs
    text= nltk.Text(f.read().split('\n'))
    freqd = FreqDist(text)
    most_common = freqd.most_common(15)
    # Sorting according to Type of entity
    for el in most_common:
        print el 

ner_chunk(sents)
experiments()

