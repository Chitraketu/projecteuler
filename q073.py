import math
import time
from fractions import Fraction as f


def isCoprime(a,b):
	return math.gcd(a,b) == 1


if __name__ == '__main__':
	n = 12000 

	low = 3
	high = 2
	fl = f(1,low)
	fh = f(1,high)
	start_time = time.time()
	count = 0
	for x in range(2,n+1):
		lr = (x // low ) - 1
		hr = (x // high) + 1
		for j in range(lr,hr+1):
			fr = f(j,x)
			if isCoprime(j,x) and fr > fl and fr < fh:
				count += 1
	print (count)
	print (time.time() - start_time,'seconds')