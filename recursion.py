

def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)



def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if(num==1):
		return product
	else:
		return fact_iter(num-1,num*product)

#return fact_iter(num-1,num*product)仅返回递归函数本身
#尾递归优化问题


