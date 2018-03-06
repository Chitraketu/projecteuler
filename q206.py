import math

def checkFormat(n):
	l = str(n)
	return l[0] == '1' and l[2] == '2' and l[4] == '3' and l[6] == '4' and l[8] == '5' and l[10] == '6' and l[12] == '7' and l[14] == '8' and l[16] == '9'
if __name__ == '__main__':
	x = 10203040506070809
	y = 19293949596979899
	a = int(math.sqrt(x))
	b = int(math.sqrt(y))
	print(checkFormat(x))
	for i in range(a,b+1):
		k = i%10
		if k == 3 or k == 7:
			z = i**2
			if checkFormat(z):
				print (i,z)
				break
