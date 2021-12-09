#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  

import sys

def get_input_file(demo, issue:int=None):
	print(issue)
	s = ''
	if issue is not None:
		s = str(issue).rjust(2,'0')
	return ('input{}' if not demo else 'input{}-demo').format(s)

def read_file_into_list(name='input', mapfnc = lambda x:x.strip()):
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	return [*map(mapfnc, lines)]

def read_file_into_list_of_ints(name='input'):
	"""
	Reads all lines into list and map int(x.strip()) on each.
	"""
	return read_file_into_list(name, lambda x: int(x.strip()))
	
def read_file_into_lists_of_ints(name='input', mapfnc = lambda x:x.strip()):
	"""
	Read 
	"""
	return read_file_into_list(name, lambda x: [*map(int, x.strip().split(','))])

def print_answer(part:int, demo, answer):
	print("Answer_{} = {}{}".format(part, answer, ' (demo)' if demo else ''))

def main(args):
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
