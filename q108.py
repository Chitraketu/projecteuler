from q072 import seiveSpf,getFactors
from q095 import divisors,primes,factorization
from functools import reduce

if __name__ == '__main__':
	n = 10**8
	#n = 8
	primeslist = primes(int(n)+1) 
	l = 0
	i = 180180 - 1
	count = 0
	ll = []
	while count < 10:

		l = (reduce(lambda x,y:x*y,list(map(lambda x:2*x[1]+1,factorization(i,primeslist))))+1)//2
		print (i,l)
		if l > 1000:
			ll.append((i,l,factorization(i,primeslist)))
			count += 1
		i+= 1
	for x in ll:
		print (x)
	print (1260,factorization(1260,primeslist))