
def pentagonal(k):
	return k * (3*k-1)//2;


def generatePentagonal(n):
	l = []
	for k in range(1,n):
		l.append(pentagonal(k))
		l.append(pentagonal(-1*k))
	return l

if __name__ == '__main__':
	partitions = [1,1,2,3]
	pents = generatePentagonal(10**6)

	k = 4
	while(1):
		pn = 0
		i = 0
		c = 0
		flag = False
		while (pents[i] <= k):
			if c == 2:
				flag = not flag
				c = 0
			#print (k,'-',pents[i],flag)
			if not flag:
				pn = pn + partitions[k - pents[i]]
			else:
				pn = pn - partitions[k - pents[i]]

			c += 1
			i += 1
		print (k)
		print (pn)
		if (k + 1) % 5 == 0:
			if pn % (10**6) == 0:
				print (pn)
				break
		partitions.append(pn)
		k += 1

	#print (partitions)