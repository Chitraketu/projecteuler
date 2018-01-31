import sys
import q27
import math


def has4pf(x, primes):
	global primeSets
	count = 0
	l = primes
	primeD = set()
	#print(l)
	n = 2
	'''
	while primes[n] <= math.sqrt(x):
		if x % primes[n] == 0:
			count += 1
			primeD.add(primes[n])
			if int(x/primes[n]) in primeSets:
				primeD.add(int(x/primes[n]))
				count += 1
			l = min(primes[n],int(x/primes[n]))
			x = int(x/l)
		n += 1
		if count > 4:
			return False
	'''

	for n in range(2,int(math.sqrt(x)+1)):
		if x % n == 0:
			if n in primeSets:
				primeD.add(n)
			if int(x/n) in primeSets:
				primeD.add(int(x/n))


	count = len(primeD)

	#print (primeD)
	return count == 4

def findFactors(x,primes):
	print (x)
	primeD = set()
	n = 0
	while x!= 1:
		if x % primes[n] == 0:
			primeD.add(primes[n])
			x = x / primes[n]
			n = 0
		else:
			n += 1
	print (primeD)
	return len(primeD) == 4


if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)	
	primeSets = primes
	primes = list(primes)
	primes.sort()
	print (findFactors(134044,primes))
	print (has4pf(134044,primes))
	print (findFactors(134045,primes))
	print (has4pf(134045,primes))
	print (findFactors(134046,primes))
	print (has4pf(134046,primes))
	print (findFactors(134043,primes))
	print (has4pf(134043,primes))

	n = 0
	while (1):
		if primes[n+1] - primes[n] -1 >= 4:
			for x in range(primes[n],primes[n+1]-3):
				if has4pf(x,primes) and has4pf(x+1,primes) and has4pf(x+2,primes) and has4pf(x+3,primes):
					print(x)
					sys.exit()

		n += 1
		if primes[n] > 1000000:
			break

