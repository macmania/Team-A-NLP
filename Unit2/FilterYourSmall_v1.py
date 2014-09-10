from __future__ import division
import nltk
#from nltk.probability import FreqDist
file1= open('YourSmall/1.txt')
#raw= file1.read()
#clean up the text
cleanedRaw= [line.strip() for line in file1 if len(line)>80]
file1.close()
cleanedFile1=open('CleanedYourSmall/1.txt','w')
# write only alphanumeric into cleaned file
for line in cleanedRaw:
    cleanedFile1.write(str(line))
