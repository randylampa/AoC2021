#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 02

import sys
sys.path.append('..')
import utils

def load_directions_list(fn):
	return utils.read_file_into_list(fn, lambda x: tuple(x.strip().split()))

def follow_directions(directions, init_horizontal_depth = (0,0)):
	horizontal,depth = init_horizontal_depth
	for way,dif in directions:
		#~ print(horizontal, depth)
		dif = int(dif)
		if way=='forward':
			horizontal+=dif
		elif way=='down':
			depth+=dif
		elif way=='up':
			depth-=dif
	return(horizontal, depth)

def solve_part_1():
	fn = 'input' if True else 'input-demo'
	directions = load_directions_list(fn)
	#~ print(directions)
	
	horizontal,depth = follow_directions(directions, (0,0))
	#~ print(horizontal,depth)
	
	answer = horizontal*depth
	
	print("Answer1 =", answer)

def follow_directions_aim(directions, init_horizontal_depth_aim = (0,0,0)):
	horizontal,depth,aim = init_horizontal_depth_aim
	for way,dif in directions:
		#~ print(horizontal, depth)
		dif = int(dif)
		if way=='forward':
			horizontal+=dif
			depth+=dif*aim
		elif way=='down':
			aim+=dif
		elif way=='up':
			aim-=dif
	return(horizontal, depth)

def solve_part_2():
	fn = 'input' if True else 'input-demo'
	directions = load_directions_list(fn)
	#~ print(directions)
	
	horizontal,depth = follow_directions_aim(directions, (0,0,0))
	#~ print(horizontal,depth)
	
	answer = horizontal*depth
	
	print("Answer2 =", answer)
	
def main(args):
	
	#~ solve_part_1()
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
