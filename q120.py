if __name__ == '__main__':
	r = 0
	for i in range(3,1001):
		print (i)
		r += (2*i*((i-1) // 2))
	print (r)