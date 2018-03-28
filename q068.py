import itertools

def isMagic(l):
	i = 3
	x = l[0]
	s = sum(l[:3])
	while(i<len(l)):
		if x > l[i]:
			return False
		if i == len(l)-1:
			ss = l[i]+l[i-1]+l[1]
		else:
			ss = l[i]+l[i-1]+l[i+1]
		if ss != s:
			return False
		i += 2
	return True

def transformMagic(l):
	m = []
	m += l[:3]
	i = 3
	while(i<len(l)):
		if i == len(l)-1:
			m.extend([l[i],l[i-1],l[1]])
		else:
			m.extend([l[i],l[i-1],l[i+1]])
		i += 2
	return m

if __name__ == '__main__':
	x = list(range(1,11))
	l = itertools.permutations(x)
	l = list(l)
	l = list(filter(isMagic,l))
	l = list(map(transformMagic,l))
	l = [''.join(map(str,x)) for x in l]
	l = list(filter(lambda x:len(x) == 16,l))
	print (max(l))