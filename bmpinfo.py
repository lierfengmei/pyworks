#-----------------------------------------------------------
# 编写一个bmpinfo.py ,检查任意文件是否是位图文件，如果是，
# 打印出图片大小和颜色数


import struct

def bmpinfo(s):
	try:
		s = struct.unpack('<ccIIIIIIHH',s)
		if s[0] == b'B' && s[1] == b'M':
			print('该图为Windows位图')
			print('位图大小为%d*%d,颜色数为%d' % (s[6],s[7],s[9]))
		elif:
		s[0] == b'B' && s[1] == b'A':
		print('该图为OS/2位图')
		print('位图大小为%d*%d,颜色数为%d' % (s[6],s[7],s[9]))
		else:
			print('该图不是Windows位图')
	except Exception as e:
		print(e)
	finally:
		print('finally...')


# test 测试内容
if __name__ == '__main__':
	f = open(filename,'rb')
	s = f.read(30)
	bmpinfo(s)




