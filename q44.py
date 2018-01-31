import math

def isPent(x):
	n = (1 + math.sqrt(1+24*x))/6
	#print(n)
	if n == int(n):
		return int(n)
	else:
		return -1

def pent(n):
	return (3*n*n-n)/2

if __name__ == '__main__':
	l = {}

	for x in range(2,100):
		for y in range(x+1,100):
			z = isPent(pent(x) + pent(y))
			if z > -1:
				l[(x,y)] = z

	print (l)


