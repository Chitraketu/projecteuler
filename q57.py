from fractions import Fraction as frac
import math

def seq(num):
	return frac(num.numerator* 2 + num.denominator,num.numerator)

def firstn(num):
		yield (num*(num+1)//2)

if __name__ == '__main__':
	num = frac(2,1)
	print (num)
	sqr2 = 0
	count = 0
	for x in range(1001):
		num = seq(num)
		sqr2 = 1 + frac(num.denominator,num.numerator)
		if int(math.log(sqr2.numerator,10)) != int(math.log(sqr2.denominator,10)):
			print (sqr2)
			print (int(math.log(sqr2.numerator,10)))
			print (int(math.log(sqr2.denominator,10)))
			count += 1

	print (count)
	