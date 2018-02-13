import q72
import q27
if __name__ == '__main__':
	n = 10**7
	primes = q27.generatePrimeList(n)
	spf = q72.seiveSpf(n)
	print ("primes and seive calculation finished")
	mind = 10**99
	minN = 0
	for x in range(2,n+1):
		if x in primes:
			continue
		y = q72.totient(x,spf)
		if sorted(str(x)) == sorted(str(y)):
			if x/y < mind:
				print (x,y)
				mind = x/y
				minN = x



