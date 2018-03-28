
filename = 'p081_matrix.txt'
if __name__ == '__main__':
	l = []
	with open(filename,'r')	as f:
		for line in f:
			l.append(line.rstrip().split(','))
	length = len(l)
	for x in l:
		print (x)
	psum = [[0 for _ in range(length)] for _ in range (length) ]
	s = int(l[0][0])
	psum[0][0] = int(l[0][0])
	print (s)
	for i in range(1,length):
		s += int(l[i][0])
		psum[i][0] = s
		psum[0][i] = sum(map(int,l[0][:i+1]))

	for x in range(1,length):
		for y in range(1,length):
			print (l[x][y],type(l[x][y]),x,y)
			print (int(l[x][y]))
			psum[x][y] = int(l[x][y]) + min(psum[x-1][y],psum[x][y-1])

	for x in range(length):
		print (psum[x])

	print (psum[length-1][length-1])

	