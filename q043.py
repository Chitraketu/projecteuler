import itertools

if __name__ == '__main__':
	digits = '0123456789'
	primes = [2,3,5,7,11,13,17]

	pans = itertools.permutations(digits)
	pans = [''.join(x) for x in pans]
	pans = list(map(int,pans))
	pans = list(filter(lambda x: x%2 and x%5 and len(str(x)) == 10, pans))
	print (len(pans))

	pansums = 0
	for x in pans:
		flag = True
		for i,p in enumerate(primes):
			if(int(str(x)[i+1:i+4]) % p ):
				flag = False
				break

		if flag:
			pansums += x

	print (pansums)