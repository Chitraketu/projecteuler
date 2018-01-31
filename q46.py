
import q27


def has4pf(x, primes):
	count = 0
	while x != 1:
		for p in primes:
			if x % p == 0:
				count += 1
				while x % p != 0:
					x /= p

			if count > 4:
				return False


	return count == 4


if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)	


	n = 211
	print("hellow")
	while(1):
		if has4pf(n+4,primes) and has4pf(n+3,primes) and has4pf(n+2,primes) and has4pf(n+1,primes):
			print (n)
			print ('is this it?')
			break

		n+=1
		if n >= 100000:
			break