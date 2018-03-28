# generate the quadratic formulae for getting the max number of primes as the quadratic function
#print the product of coefficients


def generatePrimeList(n):
	primes = [True]*n
	primes[0] = False
	#print(primes)
	for i in range(2,int(n**0.5)+1):
		#print(primes)
		#print(i)
		if primes[i-1]:
			for j in range(i*i,n+1,i):
				primes[j-1] = False

	seive = set()
	#print(primes)
	for i,x in enumerate(primes):
		if x:
			seive.add(i+1)
	#print (seive)
	return seive

def checkPrime(n):
	global primes
	global largestPrime
	if n < largestPrime:
		return n in primes
	else:
		isPrime = False
		for x in range(2,n**0.5):
			if n%x == 0:
				return False
		return True


def quadratic(a,b):
	n = 0
	count = 0
	while(1):
		exp = n**2+n*a+b
		if exp < 1:
			return count
		if (checkPrime(n**2+n*a+b)):
			count += 1
		else:
			break
		n += 1

	return count

if __name__ == "__main__":
	global primes
	global largestPrime
	x = int(input())
	primes = generatePrimeList(x)
	largestPrime = max(primes)
	maxc = 0
	maxp = 0
	for a in range(-999,1000):
		for b in range(-999,1000):
			counts = quadratic(a,b)
			if maxc < counts:
				maxc = counts
				maxp = a*b
				print(a,b, maxc)
	print (maxp)
