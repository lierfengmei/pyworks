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

import os

def FindFile(filename,str):

	try:
		dirlist = os.listdir(filename)
		for x in dirlist:
			tmp = os.path.join(filename,x)
			if os.path.isdir(tmp):
				FindFile(tmp,str)
			if os.path.isfile(tmp):
				if str in x:
					print(x)
	except Exception as e:
		print(e)



def checkFile(path,str):

	#	step2：查找文件名包含指定字符串的文件，并打印出相对路径
		L = os.listdir(path)
		
		for x in L:
			newpath = os.path.join(path,x)
			if os.path.isfile(newpath) and str in x:
				print(x)
			if os.path.isdir(newpath):
				checkFile(newpath,str)



	# 	L1 = [x for x in os.listdir(path) if os.path.isfile(x) and x.find(str)!=-1]
	# 	for x in L1:
	# 		print(x)

	# #	step1:列出当前目录下的所有目录的子文件
	# 	L2 = [x for x in os.listdir(path) if os.path.isdir(x)]

	# 	# if len(L2)==0:
	# 	# 	return

	# 	#print('the length is %d' % len(L2))
	# #	if(len(L2)!=0):
	# 	for x in L2:
	# 		newpath = os.path.join(path,x)
	# 	#	print(newpath)
	# 		checkFile(newpath,str)

print('\nHere is the checkFile funtion prints:')
checkFile('e:','my')
#FindFile('e:','prime')
print('\nHere is the FindFile function prints:')
FindFile('e:','my')

