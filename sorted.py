假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):

L2 = sorted(L, key=by_name)
print(L2)




# -*- coding:utf-8 -*-
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
	return t.key