from functools import reduce


#合并函数编写如下：
# def str2int(s):
# 	def fn(x,y):
# 		return 10*x + y
# 	def char2num(ch):
# 		return  {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ch]
# 	return reduce(fn,map(char2num,s))


#解释该函数，该函数的目的是把字符串转换成Int型数据。需要进行如下步骤
#1、每个char转成Num，写成子函数char2num
#2、调用char2num对str中的所有数据进行处理，其中str看成list,因此调用map函数
#3、将num合并成int函数，因为使用了10*x+y的函数，所以可以用reduce函数来合并。

# from functools import reduce

#分步函数编写如下：
# def fn(x,y):
# 	return 10*x + y
#使用dic映射调用即可。
def char2num(ch):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ch]

def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))
#注释的快捷键是：ctrl+shift+/



