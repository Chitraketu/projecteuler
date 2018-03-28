import q27
import math


if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)
	l = list(primes)
	l.sort()

	for x in range(9,1000001,2):
		if x in primes:
			continue
		flag = False
		for p in l:
			if p >= x:
				break

			y = math.sqrt((x-p)/2)
			print (y)
			if y == int(y):
				flag = True
				break

		if not flag:
			print (x)
			break

