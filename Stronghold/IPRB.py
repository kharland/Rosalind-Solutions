#!/usr/bin/python

import sys
from math import factorial as fact

with open(sys.argv[1]) as inf:
	data = inf.readline().split()
	nHomD = range(0, int(data[0])) 
	nHet = range(0, int(data[1]))
	nHomR = range(0, int(data[2]))
HOMD, HET, HOMR = 1, 2, 3

def CountDominantAleleCombos(orgA, orgB):
	Parents = [orgA, orgB]
	if HOMD in Parents: return 4; # Always dominant
	if [HET, HET] == Parents: return 3; # dominant 3/4 times
	if HET in Parents and HOMR in Parents: return 2; # dominant half the time
	else: return 0; # never dominant

def GetChanceOfDominantTraits(organisms):
	totalOutcomes = 4.0 * fact(len(organisms)) / (2*fact(len(organisms)-2)) 
	totalDominantOutcomes = 0.0
	for i in range(0, len(organisms)-1):
		for j in range(i+1, len(organisms)):
			totalDominantOutcomes += CountDominantAleleCombos(organisms[i], organisms[j])
	return totalDominantOutcomes / totalOutcomes

# Main Implementation

organisms = [HOMD for i in nHomD] + [HET  for i in nHet] + [HOMR for i in nHomR]
print GetChanceOfDominantTraits(organisms)