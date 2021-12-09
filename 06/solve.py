#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 06

import sys
sys.path.append('..')
import utils

def simulate_growth(population:list, days:int, output_progres:bool=True, output_population:bool=True):
	for day in range(days):
		grow = 0
		for n in range(len(population)):
			if population[n]==0:
				population.append(8)
				grow+=1
				population[n] = 6
			else:
				population[n]-=1
		if output_progres:
			sday = str(day+1).rjust(3)
			sgrow = str(grow).rjust(6)
			stotal = (str(len(population)) if day<50 else 'a lot').rjust(6)
			if output_population and day<10:
				print('After day {}: {}+ {} T {}'.format(sday, sgrow, stotal, population))
			else:
				print('After day {}: {}+ {} T'.format(sday, sgrow, stotal))
	return

def solve_part_1():
	fn = 'input' if True else 'input-demo'
	lines = utils.read_file_into_lists_of_ints(fn)
	#~ print(lines)
	# load initial state
	population = lines[0]
	print('Initial state:', population)

	simulate_growth(population, 80, True, False)
	#~ print('Final state:', population)
	
	answer = len(population)
	
	print("Answer1 =", answer)

def population_to_state(population_list:list)->dict:
	population_state = {x: 0 for x in range(9)}
	for member in population_list:
		population_state[member]+=1
	#~ print(population_state)
	return population_state

def simulate_growth_the_clever_way(state:dict, days:int, output_progres:bool=True):
	"""
	The clever way is in this: Hold only number of fishes in a state, do not hold state of all the fishes
	"""
	for day in range(days):
		grow = 0
		for k in state:
			if k==0:
				grow = state[k]
			else:
				state[k-1] = state[k]
			state[k] = 0
		if grow>0:
			#~ print('grow', grow)
			# change internal state
			state[6]+=grow
			# add new (8 is always zero items after iteration)
			state[8]=grow
		if output_progres:
			sday = str(day+1).rjust(3)
			sgrow = str(grow).rjust(6)
			print('After day {}: {}+ {}'.format(sday, sgrow, state))
	return

def count_population_from_state(state:dict)->int:
	return sum(state.values())

def solve_part_2():
	"""
	Do not you dare to run this with real data!!!!
	Even the 5 part init vector breaking the script (exhausting memory).. 5GB and no output...

	The hard part here is to do it even on these large numbers...
	There are like nine states (in any given day, only these states are possible).
	So the clever way should be counting number of fishes in any given state.
	{
	0:4,
	1:10,
	2:3,
	...
	}
	So any growth will be only adding into group 8, and decreasing the counter will be adding to lower state and zeroing current.
	In the end you will add number of zeroes into group 8.
	"""
	fn = 'input' if True else 'input-demo'
	lines = utils.read_file_into_lists_of_ints(fn)
	#~ print(lines)
	# load initial state
	population = lines[0]
	print('Initial state:', population)

	population_state = population_to_state(population)

	simulate_growth_the_clever_way(population_state, 256, False)
	print('Final state:', population_state)
	
	answer = count_population_from_state(population_state)
	
	print("Answer2 =", answer)

def main(args):
	
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
