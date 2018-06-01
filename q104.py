import time,math
from decimal import *

def matmul(X,Y):
	return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def findFirstNDigitsOfFib(n,k):
	goldenR = Decimal((1 + 5**(1/2))/2)
	rootF = Decimal(5**(1/2))
	logx = Decimal(math.log(goldenR,10))
	logRtf = Decimal(math.log(rootF,10))
	x = n * logx - logRtf
	return int(10**(x-int(x)+k-1))

if __name__ == '__main__':
	start = time.time()
	n_i = 5*10**5
	a = 1
	b = 1

	for i in range(3,n_i):
		c = (a + b) % (10**9)
		b = a
		a = c
		x = findFirstNDigitsOfFib(i,9)
		sc = str(c)
		sx = str(x)
		if i == 541:
			print (sc,sx)
		if '0' in sc or '0' in sx:
			continue
		if len(set(sc)) == 9 and len(set(sx)) == 9:
			print (i)
			break
	print (time.time() - start, ' seconds')
