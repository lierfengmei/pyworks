from collections import OrderedDict

#OrderedDict 可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

#这是一个FIFO的dict，当容量超出限制时，先删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):

	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity = capacity

	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0				#如果这个key在这个dict中存在，那么containsKey 设置为1，否则设置为0
		if len(self) - containKey >= self._capacity:
			last = self.popitem(last = False)
			print('remove',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)


#--------------------------------------------------------------------------------
#counter是一个简单的计数器，例如，统计字符出现的个数：

# from collections import Counter

# c = Counter()

# for ch in 'programming':
# 	c[ch] = c[ch] + 1

# print(c)

#--------------------------------------------------------------------------
from collections import Counter

count = Counter()

for ch in 'I love programming':
	count[ch] = count[ch] + 1

print(count)


#---------------------------------------------------------------------------
#如果要让记事本这样的文本处理软件能够处理二进制数据，就需要一个二进制到字符串
#的转换方法。Base64是一种最常见的二进制编码方法。
#所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加。好处是
#编码后的文本数据可以在邮件正文、网页等直接显示。

import base64
print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b''))

#常用于在URL、Cookie、网页中传输少量二进制数据

# -*- coding:utf-8 -*-
import base64

def safe_base64_decode(s):
	i=len(s)
	while i%4!=0:
		s.append(b'=')
		i = i + 1
	return base64.b64decode(s)


	return base64.b64decode(s + b'='*(-len(s)%4))



