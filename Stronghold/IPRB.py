#!/usr/bin/python

import sys
import math

if len(sys.argv) < 4:
	print "\n IPRB [k hom dom count] [m het count] [n hom rec count]\n"

nHomD, nHet, nHomR = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
HOMD, HET, HOMR = 1, 2, 3

def CountDominantAleleCombos(orgA, orgB):
	Parents = [orgA, orgB]
	if HOMD in Parents:                         return 4; # Always dominant
	if [HET, HET] == Parents:                   return 3; # dominant 3/4 times
	if HET in Parents and HOMR in Parents:      return 2; # dominant half the time
	else: return 0;                                       # never dominant

def GetChanceOfDominantTraits(organisms):
	totalOutcomes = 4.0 * math.factorial(len(organisms)) / (2*math.factorial(len(organisms)-2)) 
	totalDominantOutcomes = 0.0
	for i in range(0, len(organisms)-1):
		for j in range(i+1, len(organisms)):
			totalDominantOutcomes += CountDominantAleleCombos(organisms[i], organisms[j])
	print totalDominantOutcomes, totalOutcomes
	return totalDominantOutcomes / totalOutcomes

# Main Implementation

organisms = []
organisms.extend([HOMD for i in range(0, nHomD)])
organisms.extend([HET  for i in range(0, nHet)])
organisms.extend([HOMR for i in range(0, nHomR)])

print GetChanceOfDominantTraits(organisms)