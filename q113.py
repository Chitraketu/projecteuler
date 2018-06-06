from math import factorial as fact

def nCr_rep(n,r):
	return fact(n+r-1) // (fact(r)*fact(n-1))
if __name__ == '__main__':
	'''idea behind this problem is to use
	combination with repition to get the bouncy numbers
	i.e, increasing as well as decreasing numbers
	and then sum them all
	'''
	bCount = 0
	i = 10**1
	i_d = 1
	gogol = 10** 101
	while(i < gogol):
		#counting the increasing number between i and i*10
		#since the digits could be between 1-9, taking i_d
		# digits from 9
		inc = nCr_rep(9,i_d)

		#counting the decreasing number between i and i*10
		#since the digits could be between 0-9, taking i_d
		# digits from 9
		dec = nCr_rep(10,i_d)

		#removing the common and the zeros
		bCount += (inc + dec - 10)

		i *= 10
		i_d += 1

	print (bCount - 90)

