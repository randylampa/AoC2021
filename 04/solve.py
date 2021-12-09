#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 04

import sys
sys.path.append('..')
import utils

def bingolines_into_bingoboards(bingolines:list)->list:
	boards = []
	#~ print(bingolines)
	for t in range(int(len(bingolines)/5)):
		board = []
		start = t*(5+1) # 5 lines of table + 1 empty line
		#~ print(t, start)
		tablines = bingolines[start:start+5]
		if not tablines:
			break
		#~ print(tablines)
		for tabline in tablines:
			# split line into 3 char chunks
			board.append([*map(int,(tabline[c:c+3] for c in range(0, len(tabline), 3)))])
		boards.append(board)
	#~ print(boards)
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
	
def dump_board(board:list):
	just = 4
	print('-'*(5+5*just+1))
	for r in range(5):
		srow = '|'
		for c in range(5):
			srow+=str(board[r][c]).rjust(just) + '|'
		print(srow)
	print('-'*(5+5*just+1))
	
def dump_board_marker(board:list, marker:list):
	"""completely useless now"""
	just = 5
	tabsep = ' >-< '
	print('-'*(5+5*just+1) + tabsep + '-'*(5+5*just+1))
	for r in range(5):
		srow = '|'
		for c in range(5):
			srow+=str(board[r][c]).rjust(just) + '|'
		srow+=tabsep + '|'
		for c in range(5):
			srow+=('+' if marker[r][c] else '-').center(just) + '|'
		print(srow)
	print('-'*(5+5*just+1) + tabsep + '-'*(5+5*just+1))

def modify_board(number:int, board:list):
	changed = False
	done = False
	colpasses = [True]*5
	rowpasses = [True]*5
	for r in range(5):
		for c in range(5):
			if board[r][c] == number:
				#~ marker[r][c] = True
				board[r][c] = None
				changed = True
			# test all walked values to =None
			v = board[r][c] is None
			rowpasses[r] = rowpasses[r] and v
			colpasses[c] = colpasses[c] and v
	if sum(rowpasses)>0 or sum(colpasses)>0:
		done = True
		#~ print('WINNER!!')
		#~ dump_board(board)
		#~ print('rowpasses', rowpasses)
		#~ print('colpasses', colpasses)
	return (changed, done)
	
def calculate_answer(number:int, board:list):
	rowsums = [0]*5
	for r in range(5):
		rowsums[r] = sum([*filter(lambda x: x is not None, board[r])])
	return sum(rowsums)*number

def solve_part_1():
	fn = 'input' if True else 'input-demo'
	bingo = read_file_into_bingo(fn)
	#~ print(bingo)
	
	numbers, boards = bingo
	
	print('numbers', numbers)
	#~ print('boards', boards)
	
	answer = None
	breakAll = False	
	for taken_number in numbers:
		print('taken_number = {}'.format(taken_number))
		for board_num in range(len(boards)):
			current_board = boards[board_num]
			if len(current_board)<5:
				print('invalid board!! board_num = {}'.format(board_num), current_board)
				break
			#~ print('>>> board_num = {}'.format(board_num))
			#~ dump_board(current_board)
			changed, done = modify_board(taken_number, current_board)
			#~ print('changed = {}'.format(changed))
			if changed:
				#~ dump_board(current_board)
				pass
			#~ print('<<< board_num = {}'.format(board_num))
			if done:
				print('WINNER is board_num = {} on number {}'.format(board_num, taken_number))
				dump_board(current_board)
				answer = calculate_answer(taken_number, current_board)
				breakAll = True
				break
		if breakAll:
			break
	
	print("Answer1 =", answer)
	
def find_winning_board(number:int, boards:list, winning_boards:list):
	boardIndices = []
	for board_num in range(len(boards)):
		current_board = boards[board_num]
		if len(current_board)<5:
			print('invalid board!! board_num = {}'.format(board_num), current_board)
			break
		#~ dump_board(current_board)
		changed, done = modify_board(number, current_board)
		if done:
			#~ print('board_num = {} on number {}'.format(board_num, number))
			#~ dump_board(current_board)
			if board_num not in winning_boards:
				winning_boards.append(board_num)
			boardIndices.append(board_num)
	return boardIndices

def solve_part_2():
	fn = 'input' if True else 'input-demo'
	numbers,boards = read_file_into_bingo(fn)
	
	print('numbers', numbers)
	#~ print('boards', boards)
	
	winning_board_pos = []
	for taken_number in numbers:
		print('taken_number = {}'.format(taken_number))
		result = find_winning_board(taken_number, boards, winning_board_pos)
		#~ print(result)
		print(winning_board_pos)
		if len(winning_board_pos)==len(boards):
			break
	board_num = winning_board_pos[-1]
	print(board_num, taken_number)
	last_winnig_board = boards[board_num]
	answer = calculate_answer(taken_number, last_winnig_board)
	
	print("Answer2 =", answer)

def main(args):
	
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
