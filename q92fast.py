import time

def findSumSquare(n):
	return sum(map(lambda x:int(x)**2,list(str(n))))

if __name__ == '__main__':
	start = time.time()
	n = 10**7
	m = 600
	lm = [-1]*(n+1)
	for i in range(1,m):
		temp = i
		while temp != 1 and temp != 89:
			print (temp)
			temp = findSumSquare(temp)
		lm[i] = temp

	print ('calculation finished upto 600')

	count = lm.count(89)

	for x in range(m,n+1):
		lm[x] = lm[findSumSquare(x)]	
		if lm[x] == 89:
			count += 1

	print ('all calculations finished')

	print (count)

	print (time.time() - start,'seconds')