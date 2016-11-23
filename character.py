
L = []
n = 1
while n<= 99:
	L.append(n)
	n += 2


r = []
n = 3
for i in range(n):
	r.append(L(i))



# the last question: 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把list编程索引-元素对，这样就可以在
# for循环中同时迭代索引和元素本身啦。