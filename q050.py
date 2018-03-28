import q27

if __name__ == '__main__':
	primes = q27.generatePrimeList(1000000)
	print (len(primes))
	primesL = list(primes)
	primesL.sort()
	con_sum = 0
	con_sum_ind_i = -1
	con_sum_ind_j = -1
	con_sums = set()
	con_len = 0
	for i in range(1000):
		for j in range(i+1,1000):
			s = sum(primesL[i-1:j])
			if s in primes:
				con_sums.add((con_sum,i-1,j))
				if con_len < (j-i+1):
					con_len = j-i+1
					con_sum = s
					con_sum_ind_i = i-1
					con_sum_ind_j = j

	print (len(con_sums))
	print (con_sum, con_sum_ind_i,con_sum_ind_j)