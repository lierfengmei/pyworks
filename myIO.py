
# -*- coding:utf-8 -*-

#'满座衣冠皆老朽，黄泉故事无止休'


__author__ = 'MeiMei'

#P1:打开文件、读文件、关闭文件常见方法

try:
	f = open('helloWorld.txt','r')
	print(f.read())
finally:
	if f:
		f.close()



#P2:简洁的写法，不必显示的关闭文件描述符
with open('helloWorld.txt','r') as f:
	#按行读取
	for line in f.readlines():
		print(line.strip())



r open for reading
w open for writing
x open for exclusive creation, failing if the file already exists
a open for writing ,appending to the end of the file if it exists
b binary mode
t text mode(default)
+ open a disk file for updating 
U universal newlines mode



with open('helloWorld.txt','r')  as f:
	print(f.read())


for line in f.readlines():
	print(line.strip())