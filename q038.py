

def isPanDigital(x):
	digits = list(str(x))
	digits.sort()
	digits = list(map(int,digits))
	return len(digits) == 9 and list(range(1,10)) == digits


if __name__ == '__main__':

	maxprod = -1
	for x in range(1,10000):
		prodString = ''
		for y in range(1,10//len(str(x))+1):
			prodString += str(x*y)
		if x == 192:
			print (prodString)
		if isPanDigital(int(prodString)):
			maxprod = max(maxprod,int(prodString))
	print(maxprod)