#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

__author__ = 'Meimei'

import sys

def test():
	args = sys.argv
	if(len(args)==1):
		print('Hello world!')
	elif(len(args)==2):
		print('Hello,%s!'% args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()



面向对象编程————Object Oriented Programming (OOP)