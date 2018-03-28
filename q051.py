import itertools
import q27

def checkPrime(n,largestPrime,primes):
	if n < largestPrime:
		return n in primes
	else:
		isPrime = False
		for x in range(2,int(n**0.5)):
			if n%x == 0:
				return False
		return True

'''
idea behind this program is simple enumerations
lets say for n digit number,
we choose x digits which will be filled from 0 to 9 then
total such combinations would be n choose x
and the remainig digit places would be iterated from 10**(x-y-1) to 10**(x-y)
and from the cartesian product of both we first find the list of all the numbers
and then check for primality and if the count of such is greater than or equal to 8
then we print it
and from the console we select the least among them satisfying the result
'''
if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)	
	largestPrime = max(primes)
	print (len(primes))
	for x in range(5,7):
		for y in range(2,x-1):
			combs =	itertools.combinations(range(x),y)
			combs = list(combs)
			for z in range(10**(x-y-1),10**(x-y)):
				#print (z)
				#print (list(combs))
				for comb in list(combs):
					#print (comb)
					l = list(set(range(x)) - set(comb))
					#print (l)
					l.sort()
					zl = list(str(z))
					n = [['0']*x for _ in range(10)]
					for xx in range(10):
						i = 0
						while(i<len(l)):
							n[xx][l[i]] = zl[i]
							i += 1
						for c in comb:
							n[xx][c] = str(xx)
					n = list(map(lambda x: int(''.join(x)),n))
					count = 0
					nl = []
					for xx in n:
						if checkPrime(xx,largestPrime,primes):
							count += 1
							nl.append(xx)
					if count >=8:
						print (nl,count)
				#print (list(combs))


