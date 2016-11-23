#from functools import reduce
from functools import reduce

def fn(x,y):
	return 10*x+y


#result = reduce(fn,[1,3,5,7,9])
#print(result)

def char2num(s):
	return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

result = reduce(fn,map(char2num,'13579'))
print(result)
