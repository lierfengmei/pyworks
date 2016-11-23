# -*- coding:utf-8 -*-

def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum:
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，
或者或许会发生变化的变量。

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

如果一定要引用循环变量，方法是再创建一个函数，用该函数的
参数绑定循环变量当前的值，无论该循环变量后续如何修改，
已绑定到函数参数的值不变。


def count:
	def f(j):
		def g:
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs


count = lambda:[lambda a=b:a*a for b in range(1,4)]     









