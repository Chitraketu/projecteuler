
if __name__ == '__main__':
	
	strchan = ''
	for x in range(1,100000):
		strchan += str(x)

	print (strchan[0])
	print (strchan[14])
	print (len(strchan))

	prod = 1
	for x in range(7):
		prod *= int(strchan[10**x-1])

	print (prod)