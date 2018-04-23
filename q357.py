import q072
if __name__ == '__main__':
	n = 10**7 + 1
	spf = q072.seiveSpf(n)	
	maxi = 0
	print (q072.getFactors(64,spf))
	print (maxi)