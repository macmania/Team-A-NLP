#!/usr/bin/env python

import sys

dict = {}

for line in sys.stdin:
	if '_' not in line:
		continue
	plt = line.split('_');
	type = plt[0]
	opt = plt[1]
	if type not in dict:
		dict[type] = open(type+'.txt', 'w')
	dict[type].write(opt)

for key in dict:
	dict[key].close()
