#!/usr/bin/python

import sys

# mature[i] is the number of mature rabbits in month i.
# young[i] is the number of young rabbit pairs that will be produced in month i.
# dead is the number of rabbit pairs that will die in the current month.
# lifespan is the number of months each rabbit will live.
#
# Each month, all rabbits that are older than L months will die and stop 
# producing (d == young[i-L]).  
# 
# Without death, the number of mature rabbits would be the number of mature
# rabbits in the previous month + the number of young rabbits in the previous
# month.  With death, we just have to subtract away the number of rabbits dying
# this month, `dead`. So mature[i] = mature[i-1] + young[i-1] - dead.
#
# The number of young rabbits is just the number of mature rabbits from the
# previous month that haven't died off. So young[i] = mature[i-1]
#
# Of course total[i] = mature[i] + young[i]
#
# We always assume that we begin at the end of month 1 with 1 pair of young
# rabbits.

def numRabbits(months, lifespan=float('inf')):
  dead = 0
  mature, young, total = [0], [1], [1]
  for i in range(1, months):
    dead = 0 if i <= lifespan-1 else young[i-lifespan]
    mature.append(mature[i-1] + young[i-1] - dead)
    young.append(mature[i-1])
  total = mature[-1] + young[-1]
  return total

with open(sys.argv[1]) as inf:
  data = inf.readline().split()
  months, lifespan = int(data[0]), int(data[1])
  print(numRabbits(months, lifespan))

    

