def add_end(L=[]):
	L.append('END')
	return L


def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

#关键参数：关键字参数允许你传入0个或者任意个含参数名的参数，
#这些关键字参数在函数内自动组装成一个dict。

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
person('Jack',24,city=extra['city'],job=extrap['job'])
person('Jack',24,**extra)


#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
#至于到底传入了哪些，就需要在函数内部通过kw检查。

def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name=',name,'age=',age,'other:',kw)


#city 和 job为命名关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)

person('Jack',24,city='Beijing',job='Engineer')

#使用命名关键字参数时，要特别注意，如果没有可变参数，
#就必须加一个*作为特殊分隔符。如果缺少*，Python解释器
#将无法识别位置参数和命名参数关键字



#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数
#和命名关键字参数，组合使用。

def f1(a,b,c=0,*args,**kw)