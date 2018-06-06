from math import log
if __name__ == '__main__':
	l = []
	for i in range(2,225):
		for j in range(1,11):
			x = i ** j
			if len(str(x)) < 2:
				continue
			s = sum(map(int,str(x)))
			if s == i:
				l.append((x,s,j))
	l.sort()
	print (l[29])