import math
input_file = 'p042_words.txt'

def calcValue(word):
	s = 0
	for c in word:
		s += (ord(c)-ord('A')+1)

	return s

def isTriangle(x):
	s = math.sqrt(1 + 8*x)
	n = (s-1)/2
	print(s)
	print(n)
	return s - int(s) == 0 and n - int(n) == 0


if __name__ == '__main__':
	words = open(input_file,'r')
	words = words.read()
	print (len(words))
	words = words.split(',')
	words = list(map(lambda x: x.replace('"',''),words))
	totalCount = 0
	for x in words:
		if isTriangle(calcValue(x)):
			totalCount += 1

	print (totalCount)
