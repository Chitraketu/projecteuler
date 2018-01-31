from decimal import *

def findCycle(d):
	if d%2 == 0 or d%5 == 0:
		return -1

	k = 1
	while(1):
		if (10**k - 1 ) % d == 0:
			return k
		k += 1	

if __name__ == "__main__":
	maxp = 0
	maxd = 0
	for x in range(1000):
		p = findCycle(x)
		if maxp < p:
			maxp = p
			maxd = x

	print(maxd)
