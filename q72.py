from fractions import Fraction as f
def seiveSpf(n):
	spf = list(range(n+1))
	for x in range(4,n+1,2):
		spf[x] = 2
	i = 3
	while(i*i < n+1):
		if (spf[i] == i):
			for j in range(i*i,n+1,i):
				if (spf[j] == j):
					spf[j] = i
		i += 1

	return list(spf)

def getFactors(x,spf):
	temp = x
	factors = set() 
	while (x != 1):
		factors.add(spf[x])
		x = x // spf[x]
	return factors

def totient(n,spf):
	factors = list(getFactors(n,spf))
	t = n
	for x in factors:
		t = (t // x) * (x-1)
	return t




if __name__ == '__main__':
	n = 10**6
	#n = 8
	spf = seiveSpf(n)
	s = 0
	for x in range(1,n+1):
		#print (x,':',getFactors(x,spf))
		s += totient(x,spf)

	print (s-1)
	print ("finished")



	