def numOfRects(n,m):
	s = 0
	for i in range(1,n+1):
		for j in range(1,m+1):
			s += (n-i+1)*(m-j+1)
	return s

if __name__ == '__main__':
	probableAns = []
	for i in range(1,100):
		for j in range(i+1,100):
			temp = numOfRects(i,j)
			if  abs(temp - 2*10**6) < 1000:
				probableAns.append((temp,i,j,abs(temp-2*10**6)))
	print (probableAns,probableAns[0][1]*probableAns[0][2])
