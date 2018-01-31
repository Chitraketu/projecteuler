import math

if __name__ == '__main__':
	
	dictP = {}

	for x in range(1,1000):
		for y in range(1,1000-x+1):
			h = math.sqrt(x**2 + y**2)
			p = h + x + y
			if h - int(h) == 0 and p <= 1000:
				if p in dictP:
					dictP[p] += 1
				else:
					dictP[p] = 1

	maxP = 0
	maxCount = 0
	for x in dictP:
		if dictP[x] > maxCount:
			maxP = x
			maxCount = dictP[x]

	print (maxP)
