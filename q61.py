
def triangle(n):
	return n*(n+1) // 2

def square(n):
	return n*n

def pentagonal(n):
	return n*(3*n-1) // 2

def hexagonal(n):
	return n*(2*n-1)

def heptagonal(n):
	return n*(5*n-3) // 2

def octagonal(n):
	return n*(3*n-2) 

def findCycle(cyclicMaps,l,n,ansl):
	if len(ansl) == 7 and len(l) == 6:
		if (ansl[0] == ansl[len(ansl)-1]):
			print ('the list is complete')
			print (ansl,l)
		return 
	for x in cyclicMaps[n]:
		tempAns = ansl[:]
		tempL = l[:]
		if(x[0][0] == '0'): continue
		if(x[1] in l): continue
		if (not x[0] in cyclicMaps): continue
		tempL.append(x[1])
		tempAns.append(x[0])
		findCycle(cyclicMaps,tempL,x[0],tempAns)
	if len(cyclicMaps[n]):
		l = tempL[:]
		ansl = tempAns[:]
	return 

if __name__ == '__main__':
	cyclicMaps = {}
	n = 1
	while(1):
		t = triangle(n)
		if len(str(t)) > 4:
			break
		if (len(str(t))) == 4:
			if str(t)[:2] in cyclicMaps:
				cyclicMaps[str(t)[:2]].append((str(t)[2:],0))
			else:
				cyclicMaps[str(t)[:2]] = [(str(t)[2:],0)]
		s = square(n)
		if (len(str(s))) == 4:
			if str(s)[:2] in cyclicMaps:
				cyclicMaps[str(s)[:2]].append((str(s)[2:],1))
			else:
				cyclicMaps[str(s)[:2]] = [(str(s)[2:],1)]

		p = pentagonal(n)
		if (len(str(p))) == 4:
			if str(p)[:2] in cyclicMaps:
				cyclicMaps[str(p)[:2]].append((str(p)[2:],2))
			else:
				cyclicMaps[str(p)[:2]] = [(str(p)[2:],2)]

		hexa = hexagonal(n)
		if (len(str(hexa))) == 4:
			if str(hexa)[:2] in cyclicMaps:
				cyclicMaps[str(hexa)[:2]].append((str(hexa)[2:],3))
			else:
				cyclicMaps[str(hexa)[:2]] = [(str(hexa)[2:],3)]

		hept= heptagonal(n)
		if (len(str(hept))) == 4:
			if str(hept)[:2] in cyclicMaps:
				cyclicMaps[str(hept)[:2]].append((str(hept)[2:],4))
			else:
				cyclicMaps[str(hept)[:2]] = [(str(hept)[2:],4)]

		o = octagonal(n)
		if (len(str(o))) == 4:
			if str(o)[:2] in cyclicMaps:
				cyclicMaps[str(o)[:2]].append((str(o)[2:],5))
			else:
				cyclicMaps[str(o)[:2]] = [(str(o)[2:],5)]
		n += 1
	ansl = []
	x = list(cyclicMaps.keys())[0]
		for x in cyclicMaps:
		ansl = [x]
		findCycle(cyclicMaps,[],x,ansl)