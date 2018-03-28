import math

def nCr(n,r):
	f = math.factorial
	return int(f(n)/f(r)/f(n-r))

if __name__ == '__main__':
	
	count = 0
	m = 1000000

	for x in range(1,101):
		for y in range(1,x+1):
			if nCr(x,y) >= m:
				count += 1

	print (count)

