
class MyDog(object):
	def __len__(self):
		return 100
	def 

dog = MyDog()
print(len(dog))


def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None


class Student(object):

	name = 'Student'
	__slots__ = ('name','age')

	def __init__(self,name):
		self.name = name

	def get_score(self):
		return self.score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score must be integer!')
		if value<0 or value>100:
			raise ValueError('Score must between 0~100!')
		self.score = value






class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score must be an integer!')
		if value<0 or value<100:
			raise ValueError('Score must between 0~100 !')
		self.score = value













def score():
    doc = "The score property."
    def fget(self):
        return self._score
    def fset(self, value):
        self._score = value
    def fdel(self):
        del self._score
    return locals()
score = property(**score())
















def name():
    doc = "The name property."
    def fget(self):
        return self._name
    def fset(self, value):
        self._name = value
    def fdel(self):
        del self._name
    return locals()
name = property(**name())


s = Student('Bob')
s.score = 90       # 给实例绑定属性

def set_age(self,age):
	self.age = age

from typs import MethodType

s.set_age = MethodType(set_age,s)	# 给实例绑定一个方法
