#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 10

import sys
sys.path.append('..')
import utils

ISSUE=10

pairs = [
	('(',')', 3),
	('[',']', 57),
	('{','}', 1197),
	('<','>', 25137)
]

"""
hint:
hledej aktuálni znak v otevíracích. když ano, dej na stack. (stack.append(x))
pokud je zavírací a je stejný jak otevírací na stacku, odeber ze stacku (stack.pop()), pokud je jiný, je to chyba a zaloguj ji.
"""

def is_opening(ch)->bool:
	for pair in pairs:
		if pair[0]==ch:
			return True
	return False

def is_closing(ch)->bool:
	for pair in pairs:
		if pair[1]==ch:
			return True
	return False

def is_pair(chO, chC)->bool:
	for pair in pairs:
		if pair[0]==chO and pair[1]==chC:
			return True
	return False

def get_opening(ch)->str:
	for pair in pairs:
		if pair[1]==ch:
			return pair[0]
	return None

def get_closing(ch)->str:
	for pair in pairs:
		if pair[0]==ch:
			return pair[1]
	return None

def get_closing_points(ch)->int:
	for pair in pairs:
		if pair[1]==ch:
			return pair[2]
	return 0

def solve_part_1():
	demo = 0

	fn = utils.get_input_file(demo, ISSUE);
	#~ print(fn)

	lines = utils.read_file_into_list(fn)
	print(lines)

	errors = [] # tuple(foundchar,il,ich,expchar)
	for il in range(len(lines)):
		line = lines[il]

		stack = []
		for ich in range(len(line)):
			ch = line[ich]
			#~ print(ch)
			if is_opening(ch):
				print('found open: {}; push to stack: {}'.format(ch, ch))
				stack.append(ch)
			elif is_closing(ch):
				if is_pair(stack[-1],ch):
					cc = stack.pop()
					print('found close: {}; pop from stack: {}'.format(ch, cc))
				else:
					print('found close: {}; NOT PAIR WITH {}'.format(ch, stack[-1]))
					print('FOUND INCONSISTENCY ON LINE {}, CHAR {}'.format(il, ich))
					errors.append((ch,il,ich))
					break
		print(stack)
		if len(stack)>0:
			print('STACK NOT EMPTY ON LINE {}'.format(il))
			errors.append((None,il,ich))

	print('ERRORS', errors)

	answer = 0
	for error in errors:
		answer+=get_closing_points(error[0])

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
