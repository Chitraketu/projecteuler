import math
filename = "p099_base_exp.txt"

def transform(x):
	(a,b) = list(map(int,x.split(',')))
	return math.log(a) * b


if __name__ == '__main__':
	with open(filename,'r') as f:
		nums = f.read().splitlines()	

	numsf = map(transform,nums)

	maxi = 0
	mind = -1
	for i,x in enumerate(numsf):
		if x > maxi:
			maxi = x
			mind = i
			print (nums[i])
			print (i)

	print (mind)
