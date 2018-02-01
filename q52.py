import itertools

if __name__ == '__main__':
	x = 125874
	while(1):
		d = set(str(x))
		flag = True
		for i in range(2,7):
			if set(str(i*x)) != d:
				x+=1
				flag = False
				break

		if flag:
			print (x)
			for i in range(2,7):
				print (x*i)
			break