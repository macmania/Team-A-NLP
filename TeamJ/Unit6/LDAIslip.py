#!/usr/bin/env python

from gensim import corpora, models
from nltk.corpus import stopwords, PlaintextCorpusReader

#Call the NLTK stop words list
stoplist = stopwords.words('english')
classevent = PlaintextCorpusReader("../Islip13Rain", '.*')

files = classevent.fileids()

#get all of the words from the corpus
texts = [[word.lower() for word in classevent.words(file) if word not in stoplist and len(word) > 3] for file in files]

#Build the dictionary and the corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

#Define the LDA model and the number of topics.
notopics = 3
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=notopics)

#Printing the topic with their probabilities
print "\n\n", notopics, "Topics with their corresponding probabilities\n"
for i in range(0, lda.num_topics):
    print "Topic", i+1, ":", lda.print_topic(i)