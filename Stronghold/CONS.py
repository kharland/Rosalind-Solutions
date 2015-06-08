#!/usr/bin/python

import sys

sequences, sequencesT = [], []
concensus = ""
counts = []
nucleotides = ('A', 'C', 'G', 'T')

# Read all sequences into a matrix where the index i,j contains the jth
# character of the ith sequence and transpose that matrix.
with open(sys.argv[1]) as FASTAfile:
	sequence = ""
	for line in FASTAfile:
		if line[0] is ">":
			if len(sequence) > 0:
				sequences.append([c for c in sequence])
				sequence = ""
		else:
			sequence += line.rstrip()
	sequences.append([c for c in sequence])
sequencesT = map(list, zip(*sequences))

# Compute the profile matrix for this group of sequences.
for nucleotide in nucleotides:
	counts.append([seq.count(nucleotide) for seq in sequencesT])

# Build the consensus string from the profile matrix
for j in range(0, len(counts[0])):
	column = [counts[i][j] for i in range(0, len(nucleotides))]
	idx = max(column)
	if column.index(idx) is 0: concensus += 'A';
	elif column.index(idx) is 1: concensus += 'C';
	elif column.index(idx) is 2: concensus += 'G';
	elif column.index(idx) is 3: concensus += 'T';

print concensus
for i in range(0, len(nucleotides)):
	print ("%s:" % nucleotides[i]),
	print ' '.join(map(str,counts[i]))