from __future__ import division
import nltk
from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
import os
from nltk.corpus import PlaintextCorpusReader
collection = PlaintextCorpusReader("CollectionSmall", '.*')
classevent = PlaintextCorpusReader("Islip13Rain", '.*')

classeventText = nltk.word_tokenize(classevent.raw());
classeventPOS = nltk.pos_tag(classeventText);

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle');
classeventSents = sent_tokenizer.tokenize(classevent.raw());

from nltk.corpus import brown
from nltk.corpus import treebank

BrownAndTbankTag = nltk.corpus.brown.tagged_words() + nltk.corpus.treebank.tagged_words()
taggedWordsbaseline = dict(BrownAndTbankTag)

#evaluation of our tagger
baseline_tagger = nltk.UnigramTagger(model=taggedWordsbaseline)
baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
0.6333213994470632

def backoff_tagger(tagged_sents, tagger_classes, backoff=None):
    if not backoff:
        backoff = tagger_classes[0](tagged_sents)
        del tagger_classes[0]
 
    for cls in tagger_classes:
        tagger = cls(tagged_sents, backoff=backoff)
        backoff = tagger
 
    return backoff

from nltk.corpus import semcor
#from nltk.corpus import senseval

learnedTaggedWords = nltk.corpus.brown.tagged_sents() + nltk.corpus.treebank.tagged_sents() # + nltk.corpus.semcor.tagged_sents()

patterns = [
     (r'.*ing$', 'VBG'),               # gerunds
     (r'.*ed$', 'VBD'),                # simple past
     (r'.*es$', 'VBZ'),                # 3rd singular present
     (r'.*ould$', 'MD'),               # modals
     (r'.*\'s$', 'NN$'),               # possessive nouns
     (r'.*s$', 'NNS'),                 # plural nouns
     (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
     (r'.*', 'NN')                     # nouns (default)
]

 #creating a regex tagger
regex_tagger = nltk.RegexpTagger(patterns);
regex_tagger.evaluate(brown.tagged_sents(categories='news')) # 0.20326391789486245

compoundTagger = backoff_tagger(learnedTaggedWords, [nltk.tag.AffixTagger, nltk.tag.UnigramTagger, nltk.tag.BigramTagger, nltk.tag.TrigramTagger], backoff=regex_tagger)

compoundTagger.evaluate(brown.tagged_sents(categories='news')) # 0.9654613441533902

# doing multiple evaluations

compoundTagger.evaluate(brown.tagged_sents(categories='reviews')) # 0.9702731918238994
compoundTagger.evaluate(brown.tagged_sents(categories='humor')) # 0.9689329338557271
#compoundTagger.evaluate(semcor.tagged_sents())
