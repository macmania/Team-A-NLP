import re, os, operator
#try to fit in|at NE
locationPatternString = "((in|at)\s([a-zA-Z]{4,}|[a-zA-Z]{2,}\s[a-zA-Z]{3,}))|\s+[a-zA-Z]{3,},\s[a-zA-Z]{2,}\s[a-zA-Z]{3,}"

timePatternString = "(((on|at)\s((S|s)unday)|((T|t)uesday)|([Mm]onday)([Ww]ednesday)|([Tt]ursday)|([Ff]riday)|([Ss]aturday)),?\s([a-zA-z]*)\s([0-9]+))"

shooterPatternString = "((shooter)(\s[a-z]+\s[a-z]+))"

todPatternString = "(morning|afternoon|dusk|dawn|(d+:\d+ (pm|am)))"

numKilledPatternString = "([0-9]+) people? (died|were killed|killed|shot)"

numHurtPatternString = "([0-9]+) (injured|wounded|hurt|damaged|lived)"

gunPatternString = "((use(d|ing) a )([a-z]+))"

agePatternString = "(from? [0-9]+ (to|and) [0-9]+)"

# create the array of pattern strings
patternStrings = [locationPatternString, timePatternString, shooterPatternString, todPatternString, numKilledPatternString, numHurtPatternString, gunPatternString, agePatternString]

#allocate the pattern array
patterns = [None]*len(patternStrings)

for i in range(len(patternStrings)):
	patterns[i] = re.compile(patternStrings[i])

#print patternStrings

#locationPattern = re.compile(locationPatternString) # Compilation of regex patterns to improve repeated query efficiency

results = [dict() for x in range(len(patternStrings))];
# look through every file for match
listOfFiles = os.listdir('../../collections/SmallCollParas')
#listOfFiles= ['../../collections/SmallCollParas/5.txt']
for fileName in listOfFiles:
	f= open(os.path.join('../../collections/SmallCollParas',fileName))
    	#f= open(fileName)
    	text= f.read()
    	#print text
	for i in range(len(patterns)):
		# run regex for each pattern
    		matchList= patterns[i].findall(text)
    		#print matchList
    		for matchStr in matchList:
			if len(matchStr[0]) == 0:
				continue
        		# Increment the frequency for this attribute and word pair
        		try:
            			results[i][matchStr[0]] += 1
        		except:
            			results[i][matchStr[0]] = 1
    	f.close()   
#locationFreqTup = sorted(locDict.iteritems(), key=operator.itemgetter(1), reverse=True)

#for dict in results:
#	print dict

freqTuples = [None] * len(patterns)
for i in range(len(patterns)):
	freqTuples[i] = sorted(results[i].iteritems(), key=operator.itemgetter(1), reverse=True)
# Prints the top 10 words for each attribute.
#print "Top 20 frequent values for each attribute:"
#print "Location:", locationFreqTup[:20], "\n"

#print results

# Prints the original template.
print "Template before filling-out:\n"
print """On< date >, there was a shooting at <where>. <Shooter(s) name> attacked the<place of shooting> at <time of day>, by opening fire in a <where>. The <shooter(s)> killed<number of victims> and injured<number of victims> before <did shooter die or get caught>. The victims were <age range>, and were <targeted or random>. <Number of responders> arrived at the scene at <how long did it take to respond>.
The <shooter(s)> used a <type of weapon>, and shot<number of rounds>. They had intended on <bigger plans> following the shooting. The <shooter(s) > spent <time planning>, and planned using<resources used to plan>. The reason behind the attack was <motive>. The shooter received<punishment> for the attack.\n\n"""
# Prints the highest frequency result for each attribute in the formated template.

for t in freqTuples:
	print t[0:10]
	print ""
print '\n\n'

print "Template after filling-out:\n"

date = freqTuples[1][0]
where = freqTuples[0][0]
shooter = freqTuples[2][0]
place = ''
at = freqTuples[3][0]
numvictemsinjured = freqTuples[5][0]
numvictemskilled = freqTuples[4][0]
shooterkilled = ''
victemage = freqTuples[7][0]
numresponders = ''
responsetime = ''
weapon = freqTuples[6][0]
numrounds = ''
biggerplan = ''
timeplanning = ''
planningresources = ''
motive = ''
punishment = ''

print """On %s, there was a shooting at %s. %s attacked the %s at %s, by opening fire in a %s. The %s killed %s and injured %s before %s. The victims were %s, and were <targeted or random>. <Number of responders> arrived at the scene at <how long did it take to respond>.
The %s used a %s, and shot<number of rounds>. They had intended on <bigger plans> following the shooting. The <shooter(s) > spent <time planning>, and planned using<resources used to plan>. The reason behind the attack was <motive>. The shooter received<punishment> for the attack.""" % (date, where, shooter, place, at, place, shooter, numvictemskilled, numvictemsinjured, shooterkilled, victemage, shooter, weapon)
