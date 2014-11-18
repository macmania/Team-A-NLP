#!/usr/bin/env python

import sys
import cPickle
from cPickle import load
import re
import zipimport
import os
import operator

##reload(sys)
##sys.setdefaultencoding('utf-8')
##
##pathtojava = "/usr/bin/java";
##
##importer = zipimport.zipimporter('nltk.mod')
##nltk = importer.load_module('nltk')
##nltk.internals.config_java(pathtojava);
##nltk.data.path += ["./nltkData/"]


#killerName= 'adam lanza' # from getName in priorKnow.py
#locFreqTuple= [('at connecticut', 4828), ('in newtown', 3344), ('at sandy hook elementary school', 2578), ('at easy', 1730), ('at britain', 1719), ('in seconds', 1716), ('in connecticut', 1236), ('at least', 1195), ('in this', 1166), (' article, blog entry', 1001)]

shooter='(gunman|killer[s]?|shooter[s]?|gunmen|assassin|murderer)' #otherwise shooters,gunmen,killers

locationPatternString = "((in|at)\s([a-zA-Z]{4,}|[a-zA-Z]{2,}\s[a-zA-Z]{3,}))|\s+[a-zA-Z]{3,},\s[a-zA-Z]{2,}\s[a-zA-Z]{3,}"

timePatternString = "(((on|at)\s((S|s)unday)|((T|t)uesday)|([Mm]onday)([Ww]ednesday)|([Tt]ursday)|([Ff]riday)|([Ss]aturday)),?\s([a-zA-z]*)\s([0-9]+))"

shooterPatternString = "(shooter|shooters|gunman|gunmen)"

todPatternString = "(morning|afternoon|dusk|dawn)"

numKilledPatternString = "([0-9]+) people? (died|were killed|killed|shot)"

numHurtPatternString = "([0-9]+) (injured|wounded|hurt|damaged|lived)"

gunPatternString = "(used|using|armed with|with a|packed)[a-z ]{1,15}(handgun|rifle|pistol)" # can look for prefix for rifle and check for noun/adj 

agePatternString = "(from? [0-9]+ (to|and) [0-9]+)"

namePatternString= "((shooter|murderer|killer|gunman[\s,]+|suspect)([a-zA-Z]+\s[a-zA-Z]+))" # age at the end : ([,\s\d]*

#possibleMotiveString= "([.]?[a-z\"\']+\'?s?\spossible motive\s[a-z\s]+)"
possibleMotiveString= "([.]?[\sa-z\"\']+\'?s?\spossible motive\s[a-z\s]+)"
motivePatternString= "([a-z]+\'?s?\smotive\s[a-z\s]+)"
#motivePatternString= "([a-z]+)\smotive\s([a-z\s]+)"

#foundPatternString= "(killer|shooter|gunman)[\sa-z]{1,20}(found|caught|apprehended[a-z\s]+)"
foundPatternString= "((killer|shooter|gunman)[\sa-z]{1,10}found([a-z\s]+))"

planPatternString= "(shooter[\'s]*|killer[\'s]*|gunman[\'s])*([\'s]*)([a-z\s]{1,25} plan[a-z\s\"]+)"
                    
roundsPatternString= "fired([\s0-9a-z]+)rounds" #shot

#targetPatternString="[a-z\s]*(shooter|killer|gunman|"+killerName+")([a-z\s]*targeted[a-z\s\"]*|[a-z\s\"]*random[a-z\s\"]*)"
targetPatternString= "([a-z\s,]+shooter[a-z\s]*|[a-z\s,]+killer[a-z\s]*|[a-z\s,]+gunman[a-z\s]*)(targeted[a-z\s\"]+|(shot|fire)[a-z\s\"]*random[a-z\s\"]*)"

#---------------------------------------------------------------------------------
# create the array of pattern strings
patternStrings= [shooterPatternString, roundsPatternString,motivePatternString, possibleMotiveString]
patternStrings0 = [timePatternString, todPatternString, numKilledPatternString,
                   numHurtPatternString, agePatternString, locationPatternString]
patternStrings1= [namePatternString,gunPatternString,foundPatternString,planPatternString,targetPatternString]

#---------------------------------------------------------------------------------
#allocate the pattern array
patterns=[] 
for i in range(len(patternStrings)):
    patterns.append(re.compile(patternStrings[i]))

patterns0 = [None]*len(patternStrings0)
for i in range(len(patternStrings0)):
    patterns0[i] = re.compile(patternStrings0[i])

patterns1=[]
for i in range(len(patternStrings1)):
    patterns1.append(re.compile(patternStrings1[i]))

#---------------------------------------------------------------------------------
for line in sys.stdin:
#for line in ['../lib/CleanCollectionSmall/1.txt\n','../lib/CleanCollectionSmall/10.txt\n']:
    #fname = line.rstrip("\n").split('\t')[0]
    f = open('eventData/'+line.rstrip())
    #print line.rstrip()
    text= f.read().lower()
    #print text
    if len(text) > 0:
        for i in range(len(patterns)):
            matchList= patterns[i].findall(text) # run regex for each pattern
            #print matchList
            for matchStr in matchList:
                if len(matchStr) == 0:
                    continue
                else:
                    print '%s_2_%d\t1'%(matchStr,i) # wordMatch_2_i     1
        
        for i in range(len(patterns0)):
            matchList= patterns0[i].findall(text) # run regex for each pattern
            #print matchList
            for matchStr in matchList:
                if len(matchStr) == 0:
                    continue
                else:
                    print '%s_0_%d\t1'%(matchStr[0],i) # wordMatch_0_i     1
                    
        for i in range(len(patterns1)):
            match= patterns1[i].search(text.lower()) # run regex for each pattern
            #print matchList
            if match == None:
                continue
            else:
                print '%s_1_%d\t1'%(match.group(2),i) # wordMatch_1_i     1

