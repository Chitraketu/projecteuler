import math

if __name__ == '__main__':
	s = 0
	l = []
	for x in range(2,100):
		i = 1
		while (i == int(math.log(x**i,10))+1):
			s += 1
			l.append((x,i))
			i += 1

	print (l)
	print (s)
	#counting 1^1 as well
	print (len(l)+1)