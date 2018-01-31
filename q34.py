import math

if __name__ == '__main__':

	'''
	basic intuition
	we know that 9! = 362880
	after this number if we add the largest digit 9 at the end of it then the sum of fact
	would only go 362880*2 where as the digit adding is just like 362880 * 10 which is much greater than
	the sum of factorial
	hence we only need to check upto that point
	'''
	sumall = 0
	for x in range(10,362881):
		sumfact = 0
		for c in str(x):
			sumfact += math.factorial(int(c))
		if x == sumfact:
			sumall += x
	print (sumall)