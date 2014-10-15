def avgWordLength(wordlists):
	return sum([len(w) for w in wordlists.words()]) / len(wordlists.words())

def averageSentLength(wordlists):
	return sum(len(s) for s in wordlists.sents()) / len(wordlists.sents())

def averageReadabilityIndex(wordlists):
	return 4.71*avgWordLength(wordlists) + 0.5*averageSentLength(wordlists) - 21.43
