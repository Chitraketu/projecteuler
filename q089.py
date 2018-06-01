filename = 'p089_roman.txt'
if __name__ == '__main__':
	l = []
	count = 0
	count1 = 0
	with open(filename,'r')	as f:
		for line in f:
			l.append(line.rstrip())
			if 'VIIII' in line:
				count += 1
			elif 'IIII' in line:
				count1 += 1
			if 'LXXXX' in line:
				count += 1
			elif 'XXXX' in line:
				count1 += 1
			if 'DCCCC' in line:
				count += 1
			elif 'CCCC' in line:
				count1 += 1
			print (line.rstrip())
	length = len(l)
	print (count*3 + count1*2)