import q027

if __name__ == '__main__':
	n = 8000
	p = q027.generatePrimeList(n)
	p = list(p)
	p.sort()
	MAX = 5 * (10 ** 7)
	nums = set()
	for i,x in enumerate(p):
		if x ** 2 > MAX: continue
		for j,y in enumerate(p):
			s = x **2 + y ** 3
			if s > MAX: continue
			k = int((MAX  - s) ** (1/4))
			ind = 0
			#print (x,y,k)
			#print (p[0])
			while p[ind] <= k:
				nums.add(s+(p[ind]**4))
				ind += 1

	print (nums)
	print (max(p))
	print (len(p))
	print (max(nums))
	print (len(nums))

