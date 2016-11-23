
#permute2.py

#使用递归函数来写程式
'''
def permute(seq):
	l = len(seq)
	if 1==l:
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] +seq[i+1:]
			for x in permute(rest):
				res.append(seq[i:i+1] + x)
		return res


seq = list("123489")
thelist = permute(seq)
thelist = [''.join(x) for x in thelist]
print (thelist)
'''


def permute(seq):
	l = len(seq)
	if 1==l:
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute(rest):
				res.append(seq[i:i+1]+x)
		return res

seq = list("123456")
thelist = permute(seq)
thelist = [''.join(x) for x in thelist]
print(thelist)