from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 6
	Sat = 6


Month = Enum('Month',('Jan','Feb'))
这句话的意思是动态创建了一个枚举类Month,继承了Enum类，其含有了12个成员变量，



# metaclass是类的模板，所以必须从type类型中派生

class ListMetalclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls, name, bases, attrs)




try:
	print('try……')
	r = 10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except',e)
finally:
	print('finally')
print('END')