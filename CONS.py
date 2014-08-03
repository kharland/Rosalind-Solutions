#!/usr/bin/python

import sys

"""CMD line args & helpers"""
if len(sys.argv) < 2:
	print "\nCONS [inf Input-file-name]\n"
	sys.exit()

def mfn(a, c, g, t):
	"""MostFrequentNucleotide"""
	n = max(a, c, g, t)
	if n is a: return "A";
	if n is c: return "C";
	if n is g: return "G";
	if n is t: return "T";

"""Constants"""
A, C, G, T = 0, 1, 2, 3
HEADER, SEQUENCE = 0, 1


"""Load each sequence"""
sequences = []
with open(sys.argv[1], "r") as FASTAfile:
	for line in FASTAfile:
		if line[0] == ">":
			id = line[1:].rstrip()
			sequences.append([id,""])
		elif line[0] in ['A','G','C','T']:
			sequences[-1][SEQUENCE] += line.rstrip()


"""Create profile matrix"""
seqLen = len(sequences[0][SEQUENCE])
counts = [[0 for i in range(0, seqLen)] for i in range(0, 4)] 

for i in range(0, seqLen):
	for (header,sequence) in sequences:
		if   sequence[i] == 'A': counts[A][i] += 1;
		elif sequence[i] == 'C': counts[C][i] += 1;
		elif sequence[i] == 'G': counts[G][i] += 1;
		elif sequence[i] == 'T': counts[T][i] += 1;


"""Print consensus string and profile matrix"""
print "".join([mfn(counts[A][i], counts[C][i], counts[G][i], counts[T][i])
               for i in range(0, seqLen)])

print "A:",
for c in counts[A]:
	print c,
print ""

print "C:",
for c in counts[C]:
	print c,
print ""

print "G:",
for c in counts[G]:
	print c,
print ""

print "T:",
for c in counts[T]:
	print c,