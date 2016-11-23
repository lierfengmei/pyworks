

class Chain(object):

	def __init__(self,path = ''):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__






class Chain(object):

	def __init__(self,path=''):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s'%(self_path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__


# step:如果调用的是Chain().status.user.timeline,则第一步调用了
# 	Chain() 返回了‘’,然后调用了__getattr，返回了Chain('/status')
# 	然后调用了__getattr，返回了Chain（'/status/user')
# 	一直到最后返回了Chain('/status/user/timeline'),返回了self._path
# 	即'/status/user/timeline'



class Student(object):

	def __init__(self,name):
		self._name = name

	def __call__(self):
		print('My name is %s' % self._name)






