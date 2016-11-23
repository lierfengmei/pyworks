

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：

# -*- coding:utf-8 -*-

from functools import reduce

# def str2float(s):
# 	s1,s2 = s.split('.')
# 	return reduce(lambda x,y:10*x+y,map(char2num,s1)) + reduce(lambda x,y:10*x+y,map(char2num,s2))/(10**len(s2))
	# return result1+result2


def str2float(s):
	def char2num(keys):
		return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[keys]
	if(isinstance(eval(s),float)):
		s1,s2 = s.split('.')
		return reduce(lambda x,y:10*x+y,map(char2num,s1+s2))/(10**len(s2))
	else:
		return reduce(lambda x,y:10*x+y,map(char2num,s))

# def fn(x,y):
# 	return 10*x+y



	#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from functools import reduce
# def str2float(s):
#     def char2float(keys):
#         return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[keys]
#     if isinstance(eval(s), float) :
#         s1,s2=s.split('.')
#         return reduce(lambda x,y:x*10+y,map(char2float,s1+s2))/10**len(s2)
#     else:
#         return reduce(lambda x,y:x*10+y,map(char2float,s))
# #输出123,123.456和123.0都通过.
# print('str2float(\'123.456\') =', str2float('123.456'))



def is_odd(n):
	return n%2==1

list(filter(is_odd,[1,2,3,4,5,6]))



def not_empty(s):
	return s and s.strip()

filter(not_empty,['a','b',None,'C',''])