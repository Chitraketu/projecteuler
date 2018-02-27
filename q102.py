import math

filename = 'p102_triangles.txt'

def mag(n):
	return math.sqrt(sum(map(lambda x: x**2,n)))

def unitVector(n):
	m = mag(n)
	return list(map(lambda x: x/m,n))

def dotP(a,b):
	if not len(a) == len(b):
		return -1
	s = 0
	for i in range(len(a)):
		s += (a[i]*b[i])
	return s

def acos(n):
	return math.acos(n)

def isInsidePol(p,pol):
	origin = (0,0)
	(x,y) = p
	theta = 0
	for i in range(1,len(pol)):
		v1 = pol[i-1]
		v2 = pol[i]
		v1,v2 = unitVector(v1),unitVector(v2)
		theta += acos(dotP(v1,v2))
	v1,v2 = pol[len(pol)-1],pol[0]
	v1,v2 = unitVector(v1),unitVector(v2)
	theta += acos(dotP(v1,v2))
	theta = abs(theta)
	pis = theta - (2*math.pi)
	return abs(pis-int(pis)) < 10**(-6)

if __name__ == '__main__':
	with open(filename,'r') as f:
		triangles = f.read().splitlines()
	count = 0
	for i,t in enumerate(triangles):
		temp = t.split(',')
		templ = []
		for i in range(1,4):
			templ.append((int(temp[2*i-2]),int(temp[2*i-1])))
		count += int (isInsidePol((0,0),templ))
	print (count)