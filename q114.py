from q116 import findTotComb

if __name__ == '__main__':
	N = 50 
	comb = 0
	for i in [3,4]:
		for j in range(i,N+1,i):
			print (N-j,j,findTotComb(N-j,j//i))
			comb += findTotComb(N-j,j//i)

	print (comb+1)