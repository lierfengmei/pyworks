# -*- coding:utf-8 -*-

import itertools


natuals = itertools.count(1)

for n in natuals:
	print(n)


cs = itertools.cycle('ABC')
for c in cs:
	print(c)


ns = itertools.repeat('A',3)
for n in ns:
	print(n)


naturals = itertools.count(1)
ns = itertools.takewhile(lambda x :x <10,naturals)
list(ns)