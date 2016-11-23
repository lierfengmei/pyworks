def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs


#再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数的值不变
def count2():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))		#f(i)立即被执行了
	return fs


还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：


list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10]))


def build(x,y):
	return lambda:x*x+y*y

 定义一个能够打印日志的decorator
 it accept a function as the parameter，and return another function.
def log(func):
	def wrapper(*args,**kw):
		print('call %s:'% func.__name__)
		return func(*args,**kw)
	return wrapper

	@log
	def now():
		print('2016-06-16')

		
