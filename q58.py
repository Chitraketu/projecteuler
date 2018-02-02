import q27

def findDiagonals(l):
	inc = l[len(l)-1]-l[len(l)-2]
	inc += 2
	x = l[len(l)-1]
	r = []
	for i in range(4):
		r.append(x+inc*(i+1))

	print (r)
	return r

def checkPrime(n):
	isPrime = False
	for x in range(2,int(n**0.5)):
		if n%x == 0:
			return False
	return True


if __name__ == "__main__":
	x = 3
	den = 100
	primes = q27.generatePrimeList(1000000)
	largestPrime = max(primes)
	l = [1,3,5,7,9]
	pcount = 3
	r = []
	while (den >= 10):
		for p in r:
			if p == r[len(r)-1]: continue
			if p < largestPrime and p in primes:
				pcount += 1
			elif checkPrime(p):
				pcount += 1
		x += 2
		den = pcount/len(l)*100
		print (den)
		print (pcount)
		print (len(l))
		r = findDiagonals(l)
		l += r
	print (x-2)