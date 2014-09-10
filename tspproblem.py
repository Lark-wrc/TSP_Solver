from math import sqrt
from sys import maxint
import copy
import time

""" 
This program solves a traveling salesman problem. It takes tsp 
files as input. Further details on each sections.
Author: Bill Clark (Unless otherwise noted)
"""

#Global vars.
citycount = 0
cities = {}
shortestdistance = maxint
shortestpermuation = []
start = 0

#Permuation function by by John.
#uses a python generator to cycle through permuations.
def combi(xs, low=0):
	if low + 1 >= len(xs):
            yield xs
	else:
		for p in combi(xs, low + 1):
			yield p        
		for i in range(low + 1, len(xs)):
			xs[low], xs[i] = xs[i], xs[low]
			for p in combi(xs, low + 1):
				yield p
			xs[low], xs[i] = xs[i], xs[low]

#Does the distance formula on two lists of an ordered pair.	
def distance_math(one, two):
	x = sqrt((int(two[0]) - int(one[0]))**2 + (int(two[1]) - int(one[1]))**2)
	return x

#Asks for a file, then reads in the relevant information.
f = raw_input("enter filename: ")
start = time.time()

file = open(f, 'r')
for line in file:
	words = line.split()
	if words[0] == 'DIMENSION:':
		citycount = int(words[1])
	if words[0].isdigit():
		x = [int(words[1]), int(words[2])]
		cities[int(words[0])] = x
	else:
		pass
#Main operation loop. uses two for loops, one for the possible permuations,
#the second cycles through the permutation and does the distance formula.
for p in combi([x+1 for x in range(citycount)]):
	trip_distance = 0
	for i in range(0, len(p)):
		distance = distance_math(cities[p[i]], cities[p[(i+1)%len(p)]])
		trip_distance = trip_distance + distance
	if trip_distance < shortestdistance:
		shortestdistance = trip_distance
		shortestpermuation = copy.deepcopy(p)

#Prints out best solution.		
print shortestpermuation, 'shortest order.'
print shortestdistance, 'shortest time.'
print 'program ends: ' + repr(time.time()-start)
