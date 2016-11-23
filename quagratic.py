import math

def quagratic(a,b,c):
	x1 = (math.sqrt(pow(b,2)-4*a*c)-b)/(2*a)
	x2 = (-math.sqrt(pow(b,2)-4*a*c)-b)/(2*a)
	return x1,x2