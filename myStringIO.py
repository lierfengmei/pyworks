
import os

# 练习1： 利用os模块编写一个能实现dir -l输出的程序

# 练习2： 编写一个程序，能够在当前目录以及当前目录的所有子目录下查找
#         文件名包含指定字符串的文件，并打印出相对路径。



# 		step1:获得当前目录
# 		path = os.path.abspath()

def checkFile(path,str):

	#	step2：查找文件名包含指定字符串的文件，并打印出相对路径
		L1 = [x for x in os.listdir(path) if os.path.isfile(x) and x.find(str)!=-1]
		print(L1)

	#	step1:列出当前目录下的所有目录的子文件
		L2 = [x for x in os.listdir(path) if os.path.isdir(x)]

		# if len(L2)==0:
		# 	return

		#print('the length is %d' % len(L2))
		for x in L2:
			newpath = os.path.join(path,x)
			print(newpath)
			checkFile(newpath,str)


# test
#path = os.path.abspath('.')
checkFile('e:','my')

if value>a:
	value = a
if value<b:
	value = b

value = min(a,max(value,b))

if value:
	a = 1
else:
	a = 2

a=1 if value else 2

# def FindFile(filename,value):

# 	try:
# 		dirlist = os.listdir(filename)
# 		for x in dirlist:
# 			tmp = os.path.join(filename,x)
# 			if os.path.isdir(tmp):
# 				FindFile(tmp,value)
# 			elif os.path.isfile(tmp):
# 				if value in x:
# 					print(tmp)
# 	except Exception as e:
# 		print(e)


# FindFile('.','my')


d = dict(name = 'Bob', age = 20, score = 88)

d['name']  = 'Bill'

d.name = 'Michael'

把变量从内存中变成可存储或传输的过程称之为序列化，在Python中
交pickling
其他语言中叫做 serialization, marshalling,flattening ect