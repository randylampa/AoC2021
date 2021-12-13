#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 08

import sys
sys.path.append('..')
import utils

ISSUE=8

digits = {
	0: 'abcefg',
	1: 'cf',
	2: 'acdeg',
	3: 'acdfg',
	4: 'bcdf',
	5: 'abdfg',
	6: 'abdefg',
	7: 'acf',
	8: 'abcdefg',
	9: 'abcdfg',
}

def get_candidate(seg:str)->list:
	candidates = []
	for item in digits.items():
		#~ print(item)
		if len(seg)==len(item[1]):
			candidates.append(item)
	return candidates

def read_file_into_sevseg(fn:str)->list:
	sevseg = utils.read_file_into_list(fn, lambda x:[*map(lambda y:y.strip().split(' '), x.strip().split(' | '))])
	#~ print(sevseg)
	return sevseg

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	sevseg = read_file_into_sevseg(fn)
	#~ print(sevseg)

	found_certain = []
	
	for segin,segout in sevseg:
		#~ print(segin, segout)
		for seg in segout:
			#~ print('seg', seg)
			candidates = get_candidate(seg)
			#~ print('candidates', candidates)
			if len(candidates)==1:
				found_certain.append((seg, candidates[0]))

	print('found_certain', found_certain)
	
	answer = len(found_certain)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 1

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	sevseg = read_file_into_sevseg(fn)
	#~ print(sevseg)

	print('Part 2 not solved yet')
	
	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)

def main(args):
	
	solve_part_1()
	
	#~ solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
