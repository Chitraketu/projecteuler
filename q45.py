import q44
import math

def isHex(x):
	n = (1 + math.sqrt(1+8*x))/4
	if n == int(n):
		return int(n)
	else:
		return -1

def triangle(x):
	return int(x*(x+1)/2)
if __name__ == '__main__':
	
	a = 286
	while(1):
		t = triangle(a)
		p = q44.isPent(t)
		h = a*(2*a-1)
		print (p,h)
		if q44.isPent(t) != -1 and isHex(t) != -1:
			print (t)
			break

		a += 1
