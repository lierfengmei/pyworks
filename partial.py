import functools

int2 = functools.partial(int,base=2)

# 固定了base
kw = {'base':2}

#当函数的参数个数太多，需要简化时，使用functools.partial可以
#创建一个新的函数，该函数可以固定原函数的部分参数，从而在调用时
#更加简单。