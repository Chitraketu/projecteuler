def isPalin(x):
	strx = str(x)
	for i,c in enumerate(strx):
		if not c == strx[len(strx)-1-i]:
			return False
	return True

def boolean(x):
	result = ''
	while(x):
		rem = x%2
		x = x//2
		result = str(rem)+result
	return result

if __name__ == '__main__':
	sumpalin = 0
	palinList = []
	for x in range(1000000):
		if x%2 == 0: 
			continue
		if isPalin(x):
			palinList.append(x)

	for x in palinList:
		if isPalin(boolean(x)):
			sumpalin += x

	print(boolean(212))
	print (sumpalin)