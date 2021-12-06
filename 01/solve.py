#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 01

import sys
sys.path.append('..')
import utils

def number_of_increases(inpList):
	if len(inpList)<1:
		return None
	ni = 0; previ = inpList[0]
	for curri in inpList:
		if curri>previ:
			ni+=1
		previ=curri
	return ni
	
def solve_part_1():
	fn = 'input' if True else 'input-demo'
	inpList = utils.read_file_into_list_of_ints(fn)
	#~ print(inpList)
	
	ni = number_of_increases(inpList)
	print(ni)
	
def sliding_window_sum(inpList, windowWidth = 3):
	inpList2 = [];
	for i in range(0, (len(inpList) - windowWidth) + 1):
		#~ print(i, inpList[i], inpList[i:i+windowWidth])
		inpList2.append(sum(inpList[i:i+windowWidth]))
	return inpList2

def solve_part_2():
	fn = 'input' if True else 'input-demo'
	inpList = utils.read_file_into_list_of_ints(fn)
	#~ print(inpList)
	
	inpList2 = sliding_window_sum(inpList, 3)
	#~ print(inpList2)
	
	ni = number_of_increases(inpList2)
	print(ni)

def main(args):
		
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
