#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 09

import sys
sys.path.append('..')
import utils

ISSUE=9

def is_lowest(lines:list, r:int, c:int, mr:int, mc:int, dump:bool=False)->bool:
	x = lines[r][c]
	xl = lines[r][c-1] if c>0 else 10
	xr = lines[r][c+1] if c<(mc-1) else 10
	xt = lines[r-1][c] if r>0 else 10
	xb = lines[r+1][c] if r<(mr-1) else 10
	#~ print('{} neighbors {} {} {} {}'.format(x,xl,xt,xr,xb))
	#~ print(x)
	isLow = x<xl and x<xr and x<xt and x<xb
	if isLow and dump:
		print('{} is lowest of neighbors {} {} {} {}'.format(x,xl,xt,xr,xb))
	return isLow

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""
	lines = utils.read_file_into_list(fn, lambda x: [*map(int, list(x.strip()))])
	#~ print(lines)
	mr = len(lines)
	mc = len(lines[0])
	risk_level = 0
	for r in range(mr):
		for c in range(mc):
			x = lines[r][c]
			#~ print(r,c,x)
			if is_lowest(lines,r,c,mr,mc,False):
				#~ print('on r{}c{} is lowest'.format(r,c))
				risk_level += x + 1

	answer = risk_level

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)

def solve_part_2():
	demo = 1

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""

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
