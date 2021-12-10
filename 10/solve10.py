#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2021 - 10

import sys
sys.path.append('..')
import utils

ISSUE=10

pair = [('(',')'), ('[',']'), ('{','}'), ('<','>')]

"""
hint:
hledej aktuálni znak v otevíracích. když ano, dej na stack. (stack.append(x))
pokud je zavírací a je stejný jak otevírací na stacku, odeber ze stacku (stack.pop()), pokud je jiný, je to chyba a zaloguj ji.
"""

def solve_part_1():
	demo = 1

	fn = utils.get_input_file(demo, ISSUE);
	print(fn)
	"""Do something here >>>"""

	print('Part 1 not solved yet')
	
	answer = None

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
	
	solve_part_2()
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
