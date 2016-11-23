

#calc.py
'''
def calc(seq):
	maximum  = 0
	max_item = []
	for i in seq:
		product  = (i[0]*100+i[1]*10+i[2])*(i[3]*10+i[4])
		if product>maximum:
			maximum = product
			max_item = i
		elif product== maximum:
			max_item += "," + i
	return max_item,maximum


seq = [[5,6,7,8,9],[5,6,7,9,8]]
max_item,maximum = calc(seq)
print ("Maximum at", max_item, ",product", maximum)
'''

# step1
'''
def calc(seq):
	maximum = 0
	max_item = []
	for i in seq:
		product = (i[0]*100+i[1]*10+i[2])*(i[3]*10+i[4])
		if(product>maximum):
			maximum = product
			max_item = i
		elif product==maximum:
			max_item += i
	return max_item,maximum


seq = [[1,2,3,4,5],[5,4,3,2,1,],[5,4,3,2,1,],[3,4,5,2,1]]
max_item,Maximum = calc(seq)
print("Maximum at",max_item,",product",Maximum)
'''

#改成字符串
def calc(seq,where):
	maximum,max_item = 0,[]
	for i in seq:
		product = int(i[:where]) * int(i[where:])
		if product > maximum:
			maximum,max_item = product,i
		elif product == maximum:
			max_item += ',' + i
	print ("Maximum at ",max_item,",product",maximum)

if __name__ == "__main__":
	seq = ["56789","56798","56798","12345"]
	where = 3
	calc(seq,where)








