#使用埃氏筛选法筛选出素数

#构造一个从3开始的奇数序列，注意，这是一个generator
# #并且是一个无限序列
# def _odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield n

# #筛选函数
# def _not_divisible(n):
# 	return lambda x: x%n > 0

# #定义一个生成器，不断返回下一个素数
# def primes():
# 	yield 2
# 	it = _odd_iter()	#初始化序列
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisible(n),it)

# def fn(x):
# 	return x%n>0





def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x:x%n>0

def prime():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)

#打印1000以内的素数
for n in prime():
	if(n<500):
		print(n)
	else:
		break

