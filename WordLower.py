# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：



# 函数：输入字符串，将每个word变成首字母大写，其他字母小写的word

def normalize(name):
	return name.capitalize()
#	return name.lower()
#	name[0] = name[0] -32
	#name[0]=toUpper(name[0])

# def toUpper(ch):
# 	return ch-32

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)

