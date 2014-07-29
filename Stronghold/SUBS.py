#!/usr/bin/python

import sys

if len(sys.argv) < 3:
	print "\nSUBS [needle] [haystack]\n"
	sys.exit()

needle, haystack = str(sys.argv[1]), str(sys.argv[2])
target = 0

while target < len(haystack):
	target = haystack.find(needle, target)
	if target < 0:
		break
	else:
		target += 1
		print target,