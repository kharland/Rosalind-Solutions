#!/usr/bin/python

import sys

with open(sys.argv[1]) as inf:
  haystack = inf.readline().rstrip()
  needle = inf.readline().rstrip()
  pos = 0
  while pos < len(haystack):
    pos = haystack.find(needle, pos) + 1
    if pos == 0: break;
    else: print pos,;