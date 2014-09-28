import nltk
from nltk.corpus import brown
from nltk.corpus import treebank
from cPickle import dump
from BrownAndTreebank import BrownAndTbankTag
from nltk.corpus import semcor

#Simple tagger trained with brownAndTreebank tags, tested with reuters tags
simple_tagger = nltk.UnigramTagger(BrownAndTbankTag)
simple_tagger.tag('rain')
#simple_tagger.evaluate()

# Trigram tagger
all_sents=brown.tagged_sents()+treebank.tagged_sents()
size = int(len(all_sents) * 0.9)
train_sents=all_sents[:size]
test_sents=all_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
t3.evaluate(test_sents)

# Storing our Trigram tagger
output = open('TrigramTagger.pkl', 'wb')
dump(t2, output, -1)
output.close()