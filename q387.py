import q27

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
#miller-rabin primality test 
def is_prime(n,_known_primes, _precision_for_huge_n=16,):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 

if __name__ == '__main__':
	harshad = [(i,i) for i in range(1,10)]
	xx = 0
	prevxx = 0

	_known_primes = [2, 3]
	_known_primes += [x for x in range(5, 1000, 2) if is_prime(x,_known_primes)]

	while(harshad[len(harshad)-1][0]<10**12):
		tempHarshad = harshad[prevxx:]
		temp2H = []
		for ii in range(len(tempHarshad)):
			for i in range(10):
				if (tempHarshad[ii][0]*10 + i) %  (tempHarshad[ii][1] + i) == 0:
					temp2H.append((tempHarshad[ii][0]*10+i,tempHarshad[ii][1]+i))
		prevxx = len(harshad)
		xx += len(temp2H)
		harshad.extend(temp2H)
	strong_harshad = list(filter(lambda x: is_prime(x[0]//x[1],_known_primes), harshad))
	s = 0
	for x in strong_harshad:
		for i in [1,3,7,9]:
			if is_prime(x[0]*10+i,_known_primes) and len(str(x[0]*10+i))>2:
				s += (x[0]*10+i)
	print (s)
