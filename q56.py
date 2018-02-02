
def sumOfDig(x):
	s = 0
	while (x > 0):
		r = x % 10
		s = s + r
		x = x//10
	return s

if __name__ == '__main__':
	maxsum = 0
	for x in range(100):
		for y in range(100):
			maxsum = max(maxsum,sumOfDig(x**y))

	print (maxsum)