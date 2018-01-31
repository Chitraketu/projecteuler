if __name__ == '__main__':
	
	s = 0
	for x in range(1,1001):
		s += (x**x % (10**10))
		s = s% (10**10)

	print (s)