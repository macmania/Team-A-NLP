# -*- coding: utf-8 -*-
from subprocess import call
import sys
import time
name = sys.argv[1]
numcom = 0
if len(sys.argv) > 2:
	numcom = int(sys.argv[2])
def one():
	args1 = ['mahout', 'seqdirectory', '-i', name, '-o', name+'Seq']
	print " ".join(args1)
	call(args1)
	time.sleep(2)

def two():
	args2 = ['mahout seq2sparse -i', name+'Seq', '-o', name+'Vectors', "--namedVector"]
	print " ".join(args2)
	call(args2)
	time.sleep(2)
def three():
	args3 = ['mahout canopy -i', name+'Vectors/tfidf-vectors', '-o', name+'Centroids', '-dm org.apache.mahout.common.distance.SquaredEuclideanDistanceMeasure ‐t1 300 -t2 200']
	print " ".join(args3)
	call(args3)
	time.sleep(2)
def four():
	args4 = ['mahout clusterdump -dt sequencefile -d', name+'Vectors/dictionary.file-*', '-i', name+'Centroids/clusters-0-final', '-o report.txt', '--pointsDir', name+'Clusters/clusteredPoints']
	print " ".join(args4)
	call(args4)
	time.sleep(2)

funcs = [one, two, three, four]
for i in range(numcom, 4):
	funcs[i]();
