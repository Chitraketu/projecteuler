import time

def findSmallestPerm(n):
	return int(''.join(sorted(list(str(n)))))

if __name__ == '__main__':

	start = time.time()

	n = 10**7
	#n = 28
	sn = [-1]*(n+1)
	for x in range(2,n+1):
		temp = x
		if sn[temp] != -1:
			continue
		print (temp)
		temp = findSmallestPerm(temp)
		tl = [x]
		while temp != 1 and temp != 89:
			temp = sum(map(lambda x:int(x)**2,list(str(temp))))
			temp = findSmallestPerm(temp)
			tl.append(temp)
			if sn[temp] != -1:
				temp = sn[temp]
		for tle in tl:
			sn[tle] = temp
		sn[x] = temp

	print (sn.count(89))

	print (time.time()-start, 'seconds')


