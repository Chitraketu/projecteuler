
if __name__ == '__main__':
	a = 345
	d = dict()
	maxcount = 5
	l = []
	while(1):
		x = a**3
		x = ''.join(sorted(list(str(x))))
		if x in d:
			d[x].append(a)
			if len(d[x]) == 6:
				break
		else:
			d[x] = [a]
		a += 1

	print (d['01234566'])
	for x in d:
		if len(d[x]) >= 5:
			print (x,':',d[x])
