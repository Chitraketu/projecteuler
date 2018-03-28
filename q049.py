import q27
import itertools

def isArithmeticSeq(arr):
	return arr[0]+arr[2] == 2*arr[1]


if __name__ == '__main__':
	l = q27.generatePrimeList(10000)	
	r = q27.generatePrimeList(1000)
	primeSet = l.difference(r) 
	primes = list(primeSet)
	primes.sort()
	print (len(primes))
	permutes = list(map(int,[''.join(x) for x in list(itertools.permutations(str(1487)))]))
	print (permutes)
	for x in primes:
		permutes = list(map(int,[''.join(x) for x in list(itertools.permutations(str(x)))]))
		count = 0
		seq = set()
		for y in permutes:
			if y in primeSet:
				count += 1
				seq.add(y)

		if len(seq) >= 3:
			for x in list(itertools.combinations(seq,3)):
				if isArithmeticSeq(list(x)):
					print (x[0],x[1],x[2])



			