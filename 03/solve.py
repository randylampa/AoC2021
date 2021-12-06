#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 03

import sys
sys.path.append('..')
import utils

def solve_part_1():
	fn = 'input' if True else 'input-demo'
	inpList = utils.read_file_into_list(fn)
	#~ print(inpList)
	
	n = 0
	outs = [0]*len(inpList[0])
	for inBin in inpList:
		i = 0
		for ch in inBin:
			outs[i]+= 1 if ch=='1' else 0
			i+=1
		n+=1
	print(outs, n)
	
	gamma_rate_bin = "".join([*map(lambda x: '1' if x > n-x else '0',outs)])
	gamma_rate = int(gamma_rate_bin,2)
	print('gamma_rate =', gamma_rate_bin, gamma_rate)
	
	epsilon_rate_bin = "".join([*map(lambda x: '1' if x < n-x else '0',outs)])
	epsilon_rate = int(epsilon_rate_bin,2)
	print('epsilon_rate =', epsilon_rate_bin, epsilon_rate)
	
	answer = gamma_rate * epsilon_rate
	
	print("Answer1 =", answer)

def solve_part_2():
	print('Part 2 not solved yet')
	
	answer = None
	
	print("Answer2 =", answer)

def main(args):
	
	solve_part_1()
	
	#~ solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
