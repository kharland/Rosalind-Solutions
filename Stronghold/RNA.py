#!/usr/bin/python3.3

import sys

with open(sys.argv[1], "r") as datafile:
  for line in datafile:
    print line.replace('T','U')
