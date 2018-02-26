import math

def pythogoreanTriplets(limits):
	c,m = 0,2
	triplets = []
	while c < limits:
		for n in range(1,m):
			if not math.gcd(m,n) == 1:
				continue
			if m%2 == 1 and n%2 == 1:
				continue
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			if c > limits:
				break
			triplets.append((a,b,c))
			k = 1
			while (c*k < limits):
				k += 1
				triplets.append((a*k,b*k,c*k))
		m += 1
	return triplets
if __name__ == '__main__':
	n = 1.5 * (10**6)
	#n = 20
	l = pythogoreanTriplets(n+1)	
	dl = dict() 
	for x in l:
		if sum(x) in dl:
			dl[sum(x)].append(x)
		else:
			dl[sum(x)] = [x]
	count = 0
	for x in sorted(dl.keys()):
		if x > n:
			break
		if len(dl[x]) == 1:
			#print (x)
			count += 1
	print (count)
