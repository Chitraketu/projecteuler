def rev(x):
	s = x
	reverse = 0
	while (s > 0):
		r = s % 10
		reverse = reverse * 10 + r
		s = s//10
	return reverse

def isPalin(x):
	return x == rev(x)
if __name__ == '__main__':
	count = 0
	maxiter = 50
	print (rev(312))
	for x in range(2,10001):
		y = x + rev(x)
		iter = 1
		flag = True
		while (not isPalin(y)):
			y = y + rev(y)
			iter += 1
			if iter == maxiter:
				flag = False
				break

		if not flag:
			count += 1
		else:
			print(x)

	print (count)
