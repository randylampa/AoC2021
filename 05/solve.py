#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 05

import sys
sys.path.append('..')
import utils

def read_file_into_list_of_lines__golf(fn:str)->list:
	"""
	codegolf version

	In reality, tuples would be changed to lists, 'cos [because] list(a) can be shortened to [*a] while tuple(a) can not.
	Code would be 8 byte shorter
	"""
	x = utils.read_file_into_list(fn)
	return[*map(lambda y:tuple(map(lambda z:tuple(map(int,z.split(','))),y.split(' -> '))),x)]
	
def read_file_into_list_of_lines(fn:str)->list:
	"""
	rozepsaná verze funkce read_file_into_list_of_lines__golf

	výhoda tohoto řešení: bude fungovat i kdyby byly na řádku M bodů a i kdyby body byly N-rozměrné

	0,9,1 -> 5,9,8 -> 2,0,8
	"""
	slines = utils.read_file_into_list(fn)
	#~ print(slines)
	
	list_of_lines = []
	
	# sPoint rozdělit na list podle ','; na každý prvek zavolat int(); převést na n-tici
	f_sPoint2tPoint = lambda sPoint:tuple(map(int,sPoint.split(',')))
	
	for sline in slines:
		# rozdělit řádek podle ' -> '; na každý prvek zavolat f_sPoint2tPoint; převést na n-tici
		tLine = tuple(map(f_sPoint2tPoint,sline.split(' -> ')))
		
		# přidat do výstupního seznamu
		list_of_lines.append(tLine)
		
	#~ print(list_of_lines)
	return list_of_lines

def get_max_dimensions(lines:list)->tuple:
	"""
	najde maximální velikost v každém rozměnu (M bodů, N-rozměr).
	
	lines: [tuple(tuple(int,...),...),...]
	"""
	dims = None
	for line in lines:
		for point in line:
			#~ print(point)
			pd = len(point) # point dimension
			if dims is None:
				# init dim
				dims = [0]*pd
				#~ print(dims)
			for a in range(pd):
				dims[a] = max([dims[a], point[a]])
	if dims is None:
		return ()
	#~ print(dims)
	# maximální rozměr je index, ale aby to bylo pro rezervaci listu, musí to být +1; make tuple
	return tuple(map(lambda d:d+1,dims))

def initialize_board2d(dims:tuple):
	board = []
	for r in range(dims[1]):
		board.append([0]*dims[0])
	return board

def bpoint2str(v):
	return '.' if v==0 else str(v)

def dump_board2d(board:list):
	for row in board:
		print(''.join(map(bpoint2str, row)));

def board2d_to_file(fn:str, board:list):
	f = open(fn, 'w')
	for row in board:
		f.writelines(''.join(map(bpoint2str, row))+'\n');
	f.close()

def lines_to_board2d(lines:list, board:list, process_diagonals:bool=False):
	for line in lines:
		pFrom = line[0]
		pTo = line[1]
		isHorz = pFrom[1] == pTo[1]
		isVert = pFrom[0] == pTo[0]
		#~ print(line, isHorz, isVert)
		if isHorz:
			y = pFrom[1]
			xx = [pFrom[0], pTo[0]]
			xx.sort()
			for x in range(xx[0], xx[1]+1):
				#~ print('hor',(x,y))
				board[y][x]+=1
		elif isVert:
			x = pFrom[0]
			yy = [pFrom[1], pTo[1]]
			yy.sort()
			for y in range(yy[0], yy[1]+1):
				#~ print('ver',(x,y))
				board[y][x]+=1
		elif process_diagonals:
			# only 45deg
			xx = [pFrom[0], pTo[0]]
			difX = xx[1]-xx[0]
			lengthX = abs(difX)
			xInv = int(difX/lengthX)
			
			yy = [pFrom[1], pTo[1]]
			difY = yy[1]-yy[0]
			lengthY = abs(difY)
			yInv = int(difY/lengthY)
			#~ print('diag', line, xInv, yInv)
			if lengthX == lengthY:
				#~ print('is 45deg')
				for i in range(lengthX+1):
					x = pFrom[0]+i*xInv
					y = pFrom[1]+i*yInv
					board[y][x]+=1
			else:
				print('Sorry, cannot process non-45deg line {}'.format(line))
		else:
			#~ print('line {} is neither H nor V'.format(line))
			pass
	pass

def count_crossings(board:list, cross_trigger:int):
	crossings = 0
	for row in board:
		for point in row:
			if point>=cross_trigger:
				crossings+=1
	return crossings

def solve_part_1():
	fn = 'input' if True else 'input-demo'
	#~ list_of_lines = read_file_into_list_of_lines(fn)
	#~ print(list_of_lines, 'list_of_lines')
	list_of_lines = read_file_into_list_of_lines__golf(fn)
	#~ print(list_of_lines, 'list_of_lines G')
	
	dims = get_max_dimensions(list_of_lines)
	print(dims)

	if len(dims)>2:
		print('ERROR - cannot operate with these dimmensions {}'.format(dims))
		return
	board = initialize_board2d(dims)
	#~ print(board)

	#~ dump_board2d(board)
	#~ board2d_to_file('output-'+fn, board)

	lines_to_board2d(list_of_lines, board)

	if dims[1]>80:
		# pokud je šířka více než 80 (délka řádku konzole), nemá smysl vypisovat na konzoli
		board2d_to_file('output-'+fn, board)
	else:
		dump_board2d(board)
		board2d_to_file('output-'+fn, board)
	
	answer = count_crossings(board, 2)
	
	print("Answer1 =", answer)

def solve_part_2():
	fn = 'input' if True else 'input-demo'
	list_of_lines = read_file_into_list_of_lines__golf(fn)
	#~ print(list_of_lines, 'list_of_lines G')
	
	dims = get_max_dimensions(list_of_lines)
	print(dims)

	if len(dims)>2:
		print('ERROR - cannot operate with these dimmensions {}'.format(dims))
		return
	board = initialize_board2d(dims)
	#~ print(board)

	#~ dump_board2d(board)
	#~ board2d_to_file('output2-'+fn, board)

	lines_to_board2d(list_of_lines, board, True)

	if dims[1]>80:
		# pokud je šířka více než 80 (délka řádku konzole), nemá smysl vypisovat na konzoli
		board2d_to_file('output2-'+fn, board)
	else:
		dump_board2d(board)
		board2d_to_file('output2-'+fn, board)
	
	answer = count_crossings(board, 2)
	
	print("Answer2 =", answer)

def main(args):
	
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
