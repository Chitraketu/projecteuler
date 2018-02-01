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

	print (isPent(1020))

	for x in range(2,3000):
		for y in range(x+1,3000):
			z = isPent(pent(x) + pent(y))
			if z > -1:
				l[(x,y)] = z
				r1 = isPent(pent(y)+pent(z))
				r2 = isPent(pent(x)+pent(z))
				if r1 > -1: 
					print (x,y,z,r1)
					print (pent(x))
				if r2 > -1:
					print (y,x,z,r2)
					print (pent(y))




	print (len(l))


