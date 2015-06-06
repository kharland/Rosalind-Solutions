#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "\nGC [inf FASTA input filename]\n"
	sys.exit()

ID, SEQUENCE = 0, 1
sequences = []
percentages = []

# Load each sequence
with open(sys.argv[1], "r") as FASTAfile:
	for line in FASTAfile:
		if line[0] == ">":
			id = line[1:].rstrip()
			sequences.append([id,""])
		elif line[0] in ['A','G','C','T']:
			sequences[-1][SEQUENCE] += line.rstrip()

# Get GC-content
maxSeq, maxScore = None, 0
for seq in sequences:
	total, gc = 0.0, 0.0
	for symbol in seq[SEQUENCE]:
		total += 1
		if symbol in ['G', 'C']:
			gc += 1
	if (gc/total) > maxScore:
		maxSeq = seq[ID]
		maxScore = (gc/total)

print maxSeq, maxScore*100