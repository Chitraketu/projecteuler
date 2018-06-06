
def checkBouncy(n):
	n1 = ''.join(sorted(str(n)))
	n2 = ''.join(sorted(str(n),reverse=True))
	strn = str(n)
	return not(strn == n1) and not(strn == n2)

if __name__ == '__main__':
	i = 1
	bouncyCnt = 0
	while(1):
		if checkBouncy(i):
			bouncyCnt += 1
		if bouncyCnt/i == 0.99:
			print (i)
			break
		i += 1