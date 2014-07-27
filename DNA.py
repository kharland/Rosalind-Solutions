#!/usr/bin/python3.3

import sys

A = 0
C = G = T = 0

with open(sys.argv[1], "r") as datafile:
  for line in datafile:
    for char in line:
      if char is 'A':
        A += 1
      elif char is 'C':
        C += 1
      elif char is 'G':
        G += 1
      elif char is 'T':
        T += 1

print A, C, G, T
