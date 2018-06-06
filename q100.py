from q057 import seq
from fractions import Fraction as frac

if __name__ == '__main__':
	'''
	uses Pells eqn for solving this problem
	2*(2N-1)^2 - (2K-1)^2 = 1
	i.e, X^2 - 2Y^2 = -1
	hence the solution could be approximated by 
	sqr rt of 2 using continued fraction	
	'''
	n = 10 ** 12
	num = frac(2,1)
	sqr2 = 0
	while num.numerator <= n:
		num = seq(num)
		sqr2 = 1 + frac(num.denominator,num.numerator)
		print (sqr2)
	print ((sqr2.denominator+1)//2)
