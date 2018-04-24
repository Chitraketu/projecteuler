def dot(a,b):
	p = 0
	for i in range(len(a)):
		p += a[i]*b[i]
	return p
def vec(a,b):
	return (a[0]-b[0],a[1]-b[1])

if __name__ == '__main__':
	N = 50

	points = []
	for i in range(N+1):
		for j in range(N+1):
			points.append((i,j))

	count = 0
	points = points[1:]
	#print (points)
	for i,p1 in enumerate(points):
		for j in range(i+1,len(points)):
			p2 = points[j]
			v1 = vec(p1,(0,0))
			v2 = vec(p2,(0,0))
			v12 = vec(p1,p2)
			if dot(v1,v2) == 0 or dot(v1,v12) == 0 or dot(v2,v12) == 0:
				#print (v1,v2,v12)
				count += 1
	print (count)
