#!/usr/bin/python3.3

import sys

def complement(char):
  if char is 'A': return 'T';
  if char is 'C': return 'G';
  if char is 'G': return 'C';
  if char is 'T': return 'A';

with open(sys.argv[1], "r") as datafile:
  for line in datafile:
    line = (line[::-1])[1:]
    line = "".join([complement(c) for c in line])
    print line
