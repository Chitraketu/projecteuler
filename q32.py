


if __name__ == "__main__":
	sums = 0
	pans = []
	for x in range(1,100):
		print(x)
		print(len(str(x)))
		print(9-len(str(x)))
		print((9-len(str(x)))//2)
		for y in range(101,10**(((9-len(str(x)))//2+1))):
			p = x * y
			alldigits = list(map(str,range(1,10)))
			alldigits.sort()
			alllen = len(str(x))+len(str(y))+len(str(p))
			pansets = list(set(str(x)).union(set(str(y)).union(set(str(p)))))
			pansets.sort()
			#print(alldigits)
			#print(pansets)
			if pansets == alldigits and alllen == 9:
				print (x,'X',y,'=',p)
				sums += (p)
				pans.append(p)
			
	print (pans)
	print (sum(set(pans)))
