#!/usr/bin/env python

from gensim import corpora, models
from nltk.corpus import stopwords, PlaintextCorpusReader

#Call the NLTK stop words list
stoplist = stopwords.words('english')
classevent = PlaintextCorpusReader("../../Islip13Rain", '.*')
collectionSmall = PlaintextCorpusReader("../../lib/CleanCollectionSmall", '.*')


def gentexts(evnt, topic, maxfiles=1000000, topicnum = 1):
	# generate the texts from the event
	# if a topic is set, only uses sentences that contain topic words
	files = evnt.fileids()
	amnt = min(maxfiles, len(files))
	texts = [None] * amnt
	for i in range(amnt):
		texts[i] = []
		for sent in evnt.sents(files[i]):
			words = map(lambda x: x.lower(), sent)
			ncnt = -1 if not topic else 0
			if ncnt == 0:
				for w in words:
					if w in topic:
						ncnt += 1
						break
			if ncnt < 0 or ncnt >= topicnum:
				for w in words:
					if (len(w) > 3 and w not in stoplist) or (w.isdigit() and len(w)> 1):
						texts[i] += [w]
	return texts

def findtopics(texts, num):
	#Build the dictionary and the corpus
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]

	#Define the LDA model and the number of topics.
	notopics = num
	lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=notopics)

	topics = [None] * num

	#Printing the topic with their probabilities
	#print '-------------LDA-------------------------------'
	for i in range(0, lda.num_topics):
		topics[i] = {};
		for weight, top in [pair.split('*') for pair in lda.print_topic(i).split(' + ')]:
			topics[i][top] = float(weight)
	return topics

def prettyPrintTopicDictionary(dict):
	for key in dict:
		print "(%f, %s)" % (dict[key], key), ;

# remove all the keys in the dictionary that are of below average weight
def cleanTopicDict(dict):
	if not dict:
		return
	average = sum(dict.values())/len(dict.values())
	keytorm = []
	for key in dict:
		if dict[key] < average:
			keytorm += [key]
	for key in keytorm:
		del dict[key]

def iterateLDA(evnt, iterations = 5, verbose = False, maxfiles=1000000):
	topics = [None]
	texts = None
	# run the LDA a couple of times, but removing sentences that don't contain the topic, each time
	for i in range(0, iterations):
		cleanTopicDict(topics[0]) # filtering the topics: removing every entery below the average weight
		texts = gentexts(evnt, topics[0], maxfiles=maxfiles, topicnum=1)
		topics = findtopics(texts, 1)
		if verbose:
			print "\nLDA Increment %i" % (i+1);
			prettyPrintTopicDictionary(topics[0])


def ldaclassevent():
	print "-----------------------CLASSEVENT----------------------"
	print "3 topics"
	texts = gentexts(classevent, None);
	topics = findtopics(texts, 3)
	for i in range(len(topics)):
		print "\nTopic %i:" % (i+1)
		prettyPrintTopicDictionary(topics[i])
	print "\n\n-------------------Iterated Class event------------"
	print "Note that this only prints the first topic"
	iterateLDA(classevent, verbose=True, iterations=3)

def ldasmallevent():
	print "-----------------------Collection Small----------------"
	print "5 topics"
	texts = gentexts(collectionSmall, None);
	topics = findtopics(texts, 5)
	for i in range(len(topics)):
		print "\nTopic %i:" % (i+1)
		prettyPrintTopicDictionary(topics[i])
	print "\n\n-------------------Iterated Small event------------"
	print "Note that this only prints the first topic"
	iterateLDA(collectionSmall, verbose=True, iterations=2)

# classevent
ldaclassevent();

# small event
ldasmallevent();



