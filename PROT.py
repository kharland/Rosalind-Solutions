#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "\nPROT [input-file]\n"
	sys.exit()

translationTable = {
	"UUU": "F",    "CUU": "L", "AUU": "I", "GUU": "V",
	"UUC": "F",    "CUC": "L", "AUC": "I", "GUC": "V",
	"UUA": "L",    "CUA": "L", "AUA": "I", "GUA": "V",
	"UUG": "L",    "CUG": "L", "AUG": "M", "GUG": "V",
	"UCU": "S",    "CCU": "P", "ACU": "T", "GCU": "A",
	"UCC": "S",    "CCC": "P", "ACC": "T", "GCC": "A",
	"UCA": "S",    "CCA": "P", "ACA": "T", "GCA": "A",
	"UCG": "S",    "CCG": "P", "ACG": "T", "GCG": "A",
	"UAU": "Y",    "CAU": "H", "AAU": "N", "GAU": "D",
	"UAC": "Y",    "CAC": "H", "AAC": "N", "GAC": "D",
	"UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
	"UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
	"UGU": "C",    "CGU": "R", "AGU": "S", "GGU": "G",
	"UGC": "C",    "CGC": "R", "AGC": "S", "GGC": "G",
	"UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
	"UGG": "W",    "CGG": "R", "AGG": "R", "GGG": "G"
}

def DNARNA2GenString(seq):
	try:
		return translationTable[seq]
	except KeyError:
		return seq


# We assume the input file only holds one DNA or RNA sequence
genString = ""

with open(sys.argv[1], "r") as inf:
	for line in inf:
		DNARNAseq = line
		while len(DNARNAseq) > 0:
			chunk = DNARNA2GenString(DNARNAseq[0:3])
			if chunk != "Stop":
				genString += chunk
			else:
				break
			DNARNAseq = DNARNAseq[3:]

print genString
