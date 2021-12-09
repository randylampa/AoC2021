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
	for line in board:
		print(''.join(map(bpoint2str, line)));

def board2d_to_file(fn:str, board:list):
	f = open(fn, 'w')
	for line in board:
		f.writelines(''.join(map(bpoint2str, line))+'\n');
	f.close()

def lines_to_board2d(lines:list, board:list):
	for line in lines:
		pFrom = line[0]
		pTo = line[1]
		isHorz = pFrom[1] == pTo[1]
		isVert = pFrom[0] == pTo[0]
		print(line, isHorz, isVert)
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
		else:
			#~ print('line {} is neither H nor V'.format(line))
			pass
	pass

def solve_part_1():
	fn = 'input' if False else 'input-demo'
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
	
	answer = None
	
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
