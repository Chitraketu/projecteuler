import q27
from fractions import gcd

def totient(x):
	count = 0
	for i in range(1,x):
		if gcd(i,x) == 1:
			count += 1
	return count
if __name__ == '__main__':
	primes = q27.generatePrimeList(1000)
	primes = list(primes)
	primes.sort()
	maxt = 0	
	for x in range(2,23):	
		print (x,':',totient(x),x/totient(x))
		maxt = max(maxt,x/totient(x))
	print (maxt)

	ans = 1
	i = 0
	print (primes)
	while(ans <= 1000000):
		print (primes[i])
		print (ans)
		print()
		ans *= primes[i]
		i += 1
	print (int(ans/primes[i-1]))