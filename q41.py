import q27
import itertools

def checkPrime(n):
	isPrime = False
	for x in range(2,int(n**0.5)):
		if n%x == 0:
			return False
	return True

if __name__ == '__main__':

	ans = 0
	for n in range(1,10):
		nlist = itertools.permutations(list(map(str,list(range(1,n+1)))))
		nlist = list([''.join(x) for x in nlist])
		nlist.sort()
		nlist = list(map(int,nlist))
		#nlist = list(filter(lambda x:( x%2 and x%3 and x%5 and x%7),nlist))
		#nlist = list (filter(lambda x: not(x%2 or x%3 or x%5 or x%7), nlist))
		for x in nlist:
			if checkPrime(x):
				ans = x

		print (len(nlist))
		print()
	print (ans)