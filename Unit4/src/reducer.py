#!/usr/bin/env python

from operator import itemgetter
import sys

pos_count=0
neg_count=0
unknown=0
f1=open('Relevant.txt','w')
f1=open('Noise.txt','w')
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we obtained from mapper.py
    filename, label = line.split('\t', 1)
    if label=='pos':
        pos_count += 1
        f1.write(line)
    elif label=='neg':
        f2.write(line)    
        neg_count+=1
    else :
        unknown+=1 # expect it to be 0 always
        		
    # write result to STDOUT
    print '%s\t%s' % (filename, label)
f1.close()
f2.close()
print 'Count of relevant documents: '+str(pos_count)
print 'Count of noisy documents: '+str(neg_count)
