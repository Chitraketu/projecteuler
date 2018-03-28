from fractions import Fraction as f

if __name__ == '__main__':
	a = f(2,5)
	b =  f(3,7)
	mind = 1
	minf = f(1,1,)
	for x in range(1,10**6+1):
		y = 3*x//7
		c = f(y,x)
		if c == b:
			continue
		if (b-c) < mind:
			mind = b-c
			minf = c
	print (minf)