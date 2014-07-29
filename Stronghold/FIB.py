#!/usr/bin/python

import sys

if len(sys.argv) < 3:
	print "\nFIB [n number of passed months] [k number of offspring pairs per rabbit pair]\n"
	sys.exit()

n = int(sys.argv[1])
k = int(sys.argv[2])

def generation(i, k):
	"""
	i = number of the current month
	k = number of offspring each pair of rabbits produces per month
	"""
	if i == 1: return 1;
	if i == 2: return 1;
	
	return generation(i-1, k) + k*generation(i-2, k)

print generation(n, k)