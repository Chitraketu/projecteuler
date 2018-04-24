import math
import time
''' this one is a little slow and could be improved using transformation matrices
'''
def pythogoreanTriplets(limits):
	c,m = 0,2
	triplets = []
	while c < limits:
		for n in range(1,m):
			if not math.gcd(m,n) == 1:
				continue
			if m%2 == 1 and n%2 == 1:
				continue
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			if c > limits:
				break
			mini = min(a,b,c)
			maxi = max(a,b,c)
			if abs(mini*2-maxi) == 1:
				triplets.append(tuple(sorted((a,b,c))))
		m += 1
	return triplets

if __name__ == '__main__':
	start_time = time.time()
	limits = (10**9)//3
	limitP = limits*10
	triplets = pythogoreanTriplets(limits)
	almost = list(map(lambda x:tuple((x[2],x[0]*2,x[0]*2)),triplets))
	almost = list(filter(lambda x: sum(x)<limitP,almost))
	print (almost)
	print (sum(map(lambda x: sum(x),almost)))
	print ("----- %s seconds ------" % (time.time() - start_time))