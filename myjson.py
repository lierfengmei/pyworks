# -*- coding:utf-8 -*-

import json

class Student(object):
	
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score



def student2dict(std):
	return{
	'name':std.name,
	'age':std.age,
	'score':std.score
	}

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

s = Student('Li Meimei',27,100)

json_str = json.dumps(s,default = student2dict)
#print(json.dumps(s,default = student2dict))

#print(json.dumps(s,default=lambda obj:obj.__dict__))

print(json.loads(json_str,object_hook = dict2student))
