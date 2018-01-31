import q27
import itertools

def generateCyclicPermutation(x):
	cyclicperms = []
	if len(str(x)) == 1:
		return [x]
	for i in range(len(str(x))):
		rem = x%10
		x = x//10
		x = rem*(10**(len(str(x))))+x
		cyclicperms.append(x)
	return cyclicperms

if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)
	count = 0
	#print()
	#print(type(primes))
	cyclicprimes = {}
	for x in primes:
		cyclicprimes[x] = -1
	#print(cyclicprimes)
	for x in primes:
		if cyclicprimes[x] == 0:
			continue
		perms = set(generateCyclicPermutation(x))
		#print(perms)
		
		if perms.issubset(primes):
			#print(x)
			#print(perms)
			cyclicprimes[x] = 1
			for y in perms:
				cyclicprimes[y] = 1
		else:
			cyclicprimes[x] = 0
			for y in perms:
				if len(str(y)) == len(str(x)) and y in primes:
					cyclicprimes[y] = 0
		'''if	set(map(int,itertools.permutations(str(x)))).issubset(primes):
			count += 1
		'''
	#print(cyclicprimes)
	for x in cyclicprimes:
		if cyclicprimes[x] == 1:
			#print(x,' ',cyclicprimes[x])
			count += 1
	#print(generateCyclicPermutation(197))
	print (count)
