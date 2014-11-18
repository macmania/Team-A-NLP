#!/usr/bin/env python
import sys
import nltk

# to get the stanford ner in here
from cPickle import load

outputs = {}
outputs['time'] = [];
outputs['shooterplurality'] = [];
outputs['timeofday'] = [];
outputs['numkilled'] = [];
outputs['numhurt'] = [];
outputs['gun'] = [];
outputs['agerange'] = [];
outputs['shootername'] = [];
outputs['possiblemotive'] = [];
outputs['motive'] = [];
outputs['shooterfound'] = [];
outputs['plan'] = [];
outputs['roundsfired'] = [];
outputs['target'] = [];

# an attempt to decifpher the mapping...
mapping = [['time', 'timeofday', 'numkilled', 'numhurt', 'agerange'], 
['shootername', 'gun', 'shooterfound', 'plan', 'target'], ['shooterplurality', 'roundsfired', 'motive', 'possiblemotive']]

# filter name list
filternames = ['shootername', 'gun']

stanfordTagger = None

def loadTagger():
	global stanfordTagger
	with open('stanfordNER.pickle', 'rb') as input:
		stanfordTagger = load(input)


def maparray(tup, arraynum, arrayindex):
	"""
	take the tuple and map it into the correct array
	"""
	global outputs
	loc = mapping[arraynum][arrayindex]
	add = True
	if loc in filternames:
		add &= filterNAME(tup[0])
	if add:
		outputs[loc].append(tup)

def filterNAME(st):
	global stanfordTagger
	for t in stanfordTagger.tag(st.split()):
		print t
		if t[0].lower() != 'person':
			return False
	return True

def parseline(line):
	"""
	Parse each line and add it to the correct list
	"""
	splt = line.split('\t')
	count = int(splt[1])
	splt2 = splt[0].split('_') # get the two number off the end
	arrayindex = int(splt2[-1])
	arraynum = int(splt2[-2])
	tup = (splt2[0], count)
	maparray(tup, arraynum, arrayindex)

def printoutputs():
	global outputs
	for key in outputs:
		print key,outputs[key][0:3]

def main():
	loadTagger()
	for line in sys.stdin.readlines():
		parseline(line)
	printoutputs()

main()