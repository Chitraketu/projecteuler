from itertools import compress

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0: pf.append((p, count))
    if n > 1: pf.append((n, 1))
    return pf

def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
    return divs

if __name__ == '__main__':
    n = 10**6 + 1
    primeslist = primes(int(n**0.5)+1) 
    sumD = {}
    for i in range(2,n):
        sumD[i] = sum(divisors(i)) - i
    sumD = {k:v for k, v in sumD.items() if v < n}
    print ('sumD calculation finished')
    maxK = 0
    ll = []
    for k in sumD:
        t = k
        temp = k
        count = 0
        l = [k]
        while sumD[temp] not in l:
            count += 1
            if sumD[temp] in sumD:
                l.append(sumD[temp])
                temp = sumD[temp]
            else:
                count = 0
                break
        if k == 12496:
            print (l)
        if maxK < count and sumD[temp] == k:
            maxK = count
            ll = l
            print (k,ll)

    print ('finished')
    print (ll)
    print (min(ll))

