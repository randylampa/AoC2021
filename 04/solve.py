#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 04

import sys
sys.path.append('..')
import utils

def bingolines_into_bingoboards(bingolines:list)->list:
	boards = []
	#~ print(len(bingolines))
	for i in range(0,5):
		lines = bingolines[i::6] # každá šestá
		if len(boards)==0:
			boards = len(lines)*[[None]*5]*5 # proto board
		r = 0
		for line in lines:
			# split line into 3 char chunks
			boards[r][i] = [*map(int,(line[c:c+3] for c in range(0, len(line), 3)))]
			#~ print(boards[r][i])

	return boards

def read_file_into_bingo(name:str='input', mapfnc = lambda x:x.strip())->tuple:
	f = open(name, 'r')
	# line with selected numbers
	numbers = [*map(int, f.readline().split(','))]
	# empty line
	f.readline()
	# all remaining lines
	bingolines = f.readlines()
	f.close()
	
	#~ print(bingolines)
	boards = bingolines_into_bingoboards(bingolines);
	#~ print(boards)

	return (numbers, boards)

def solve_part_1():
	fn = 'input' if False else 'input-demo'
	bingo = read_file_into_bingo(fn)
	#~ print(bingo)
	numbers, boards = bingo
	print('numbers', numbers)
	print('boards', boards)

	print('Part 1 not solved yet')
	
	answer = None
	
	print("Answer1 =", answer)

def solve_part_2():
	print('Part 2 not solved yet')
	
	answer = None
	
	print("Answer2 =", answer)

def main(args):
	
	solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
