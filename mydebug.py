# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

import pdb

def foo(s):
	n = int(s)
	assert n!=0,'n is zero'
	return 10/n


def main():
	foo('2')


main()


s = '0'
n = int(s)
pdb.set_trace()
logging.info('n=%d' % n)
print(10/n)

