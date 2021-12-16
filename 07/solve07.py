#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 07

import sys
sys.path.append('..')
import utils
import statistics
import math

ISSUE=7

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	ll = utils.read_file_into_lists_of_ints(fn)
	numbers = ll[0]
	#~ print(numbers)
	median = int(statistics.median(numbers))
	pos = round(median)
	print('align pos:', pos)

	fuel_cost = 0
	for number in numbers:
		cost = abs(pos - number)
		#~ print(number, cost)
		fuel_cost += cost
	print(fuel_cost)

	answer = fuel_cost

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	ll = utils.read_file_into_lists_of_ints(fn)
	numbers = ll[0]
	#~ print(numbers)
	mean = statistics.mean(numbers)
	print(mean)
	pos = math.ceil(mean)
	print('align pos:', pos)

	fuel_cost = 0
	for number in numbers:
		dist = abs(pos - number)
		print(number, pos, dist)
		cost = sum(range(1,dist+1))
		#~ print(number, cost)
		fuel_cost += cost
	print(fuel_cost)

	answer = fuel_cost
	# is low	 1495426
	# is high	86397082

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):

	#~ solve_part_1()

	solve_part_2()

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
