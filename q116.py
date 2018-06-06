from math import factorial as fact

def findTotComb(n,x):
	return fact(n+x) // fact(n) // fact(x)

if __name__ == '__main__':
	N = 50
	comb = 0
	# adding all comb with two tiles filling
	for i in range(2,N+1,2):
		print (N-i,i,findTotComb(N-i,i//2))
		comb += findTotComb(N-i,i//2)
	# adding all comb with three tiles filling
	for i in range(3,N+1,3):
		print (N-i,i,findTotComb(N-i,i//2))
		comb += findTotComb(N-i,i//3)
	# adding all comb with four tiles filling
	for i in range(4,N+1,4):
		print (N-i,i,findTotComb(N-i,i//2))
		comb += findTotComb(N-i,i//4)
	print (comb)



