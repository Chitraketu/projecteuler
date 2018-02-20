import q27
if __name__ == '__main__':
	denom = sorted(list(q27.generatePrimeList(5000)))
	n = 2
	while(1):
		total = [[0]*len(denom) for _ in range(n+1)]
		total[0] = [1]*len(denom)
		#print(total)
		for i in range(1,n+1):
			for j,x in enumerate(denom):
				x = total[i-x][j] if i - x >= 0 else 0 #if the number includes the denominator x
				y = total[i][j-1] if j >= 1 else 0
				total[i][j] = x + y

		print (n,total[n][len(denom)-1])
		ways = total[n][len(denom)-1]
		if ways >= 5000:
			break
		n += 1
		
		