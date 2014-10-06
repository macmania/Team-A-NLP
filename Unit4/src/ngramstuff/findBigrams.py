
f = open('Bigrams10k.txt')
listOfSentences = f.readlines()
f.close()

ourWords = ['people', 'fertilizer', 'plant', 'explosion', 'texas', 'west', 'april', 'boston', 'news', 'find', 'fire', 'time', 'point', 'volunteer', 'blast', 'state', 'town', 'community', 'marathon', 'suspect']
for line in listOfSentences:
	for word in ourWords:
		if word in line:
			print line
			continue

