

if __name__ == "__main__":
	n = int(input())
	denom = [1,2,5,10,20,50,100,200]
	total = [[0]*len(denom) for _ in range(n+1)]
	total[0] = [1]*len(denom)
	print(total)
	for i in range(1,n+1):
		for j,x in enumerate(denom):
			x = total[i-x][j] if i - x >= 0 else 0 #if the number includes the denominator x
			y = total[i][j-1] if j >= 1 else 0
			total[i][j] = x + y

	print (total[n][len(denom)-1])
