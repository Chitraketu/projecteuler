from decimal import *

if __name__ == '__main__':
	getcontext().prec = 103
	s = 0
	i = 1
	for x in range(101):
		if i*i == x:
			i += 1
			continue
		s += sum(Decimal(x).sqrt().as_tuple()[1][:100])
	print (s)
