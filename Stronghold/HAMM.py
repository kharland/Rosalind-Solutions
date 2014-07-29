#!/usr/bin/python

import sys

if len(sys.argv) < 1:
	print "\nHAMM [inf name of input file]\n"
	sys.exit()

seqA, seqB = False, False

"""assuming the file only has two lines"""
with open(sys.argv[1], "r") as inf:
	for line in inf:
		if not seqA: 
			seqA = line.rstrip()
		else:
			seqB = line.rstrip()

distance = 0
for i in range(0, len(seqA)):
	if seqA[i] != seqB[i]: 
		distance += 1

print distance