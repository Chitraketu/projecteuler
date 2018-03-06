import q27
import math

def is_prime(n):
     if n <= 1:
        return False
     elif n <= 3:
        return True
     elif n % 2 == 0 or n % 3 == 0:
        return False
     i = 5
     while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
     return True

def checkP(n,primes,maxPrime):
	if n < maxPrime:
		return n in primes
	return is_prime(n)
	

def checkCartConcatPrimes(a,b,primes,maxPrime):
	ij = int(str(a)+str(b))
	ji = int(str(b)+str(a))
	if not checkP(ij,primes,maxPrime) or not checkP(ji,primes,maxPrime):
		return False
	return True

if __name__ == '__main__':
	primeset = q27.generatePrimeList(10000000)
	maxP = max(primeset)
	primes = sorted(list(q27.generatePrimeList(8500)))
	primes = primes[:8400]
	print (primes[:5])
	print (len(primes))
	pd = dict()
	for i in range(len(primes)):
		for j in range(i+1,len(primes)):
			if checkCartConcatPrimes(primes[i],primes[j],primeset,maxP):
				if primes[i] in pd:
					pd[primes[i]].add(primes[j])
				else:
					pd[primes[i]] = set()
					pd[primes[i]].add(primes[j])

	print ('pairs calc finished')
	p2d = dict()
	skeys = sorted(pd.keys())
	for x in skeys:
		for y in pd[x]:
			if y in pd:
				intersect = pd[x].intersection(pd[y]) 
				if len(intersect) != 0:
					p2d[str(x)+','+str(y)] = pd[x].intersection(pd[y])

	p3d = dict()
	print ('triples calc finished')
	skeys = sorted(p2d.keys())
	for x in skeys:
		for y in p2d[x]:
			if y in pd:
				intersect = p2d[x].intersection(pd[y])
				if len(intersect) != 0:
					p3d[x+','+str(y)] = p2d[x].intersection(pd[y])

	p4d = dict()
	print ('quads calc finished')
	skeys = sorted(p3d.keys())
	for x in skeys:
		print (x,sorted(p3d[x]))
		for y in p3d[x]:
			if y in pd:
				intersect = p3d[x].intersection(pd[y])
				if len(intersect) != 0:
					p4d[x+','+str(y)] = p3d[x].intersection(pd[y])


	for x in sorted(p4d.keys()):
		print (x,sorted(p4d[x]))
		print(sum(map(int,x.split(','))) + sum(p4d[x]))