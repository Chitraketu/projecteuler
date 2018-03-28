import q27

def isTruncatable(x,primes):
	temp = x
	flag = True
	while(temp):
		temp = temp//10
		#print(temp,'l2r')
		if not temp in primes:
			return False

		if temp//10 == 0:
			break
	temp = x
	while(temp):
		temp = temp % (10**(len(str(temp))-1))
		#print(temp,'r2l')
		if not temp in primes:
			return False
		if temp//10 == 0:
			break
	return True

if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)
	count = 0
	sumprime = 0
	for x in primes:
		if isTruncatable(x,primes):
			sumprime += x
			count += 1
			print(x)
		if count == 11:
			break

	print(sumprime)
