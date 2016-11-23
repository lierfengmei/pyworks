# -*- coding: utf-8 -*-

# 利用@property 给 Screen 对象加上 width 和 height 属性，
# 以及一个只读属性 resolution

class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('Width must be integer!')
		if value<0:
			raise ValueError('Width must be greater than 0')
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('Height must be integer!')
		if value<0:
			raise ValueError('Height must be greater than 0!')
		self._height = value

	@property
	def resolution(self):
		return self._width*self._height


#test
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024*768 = %d ?' % s.resolution




class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object(name:%s)'% self.name
	__repr__ = __str__

	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25
		raise AttributeError('\'Student\'object has no attribute %s' % attr)
		


如果一个类想被用于for……in 循环，类似list或tuple那样，就必须
实现一个__iter__()方法，该方法返回一个迭代对象，然后Python的
for循环就会不断调用对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1  #初始化两个计数器a,b
	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b #计算下一个值
		if(self.b>10000):
			raise StopIteration()
		return self.a         #返回下一个值

	def __getitem__(self,n):
		if isinstance(n,int):	# n是索引
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):  # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b = b,a+b
			return L

#test

for n in Fib():
	print(n)





class Fib(object):

	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if(self.b>10000):
			araise StopIteration()
		return self.a

#test

for n in Fib():
	print(n)
