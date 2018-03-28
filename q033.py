
if __name__ == "__main__":
	nontrivial = []
	for x in range (10,100):
		if x % 10 == 0:
			continue
		for y in range(10,100):
			if y % 10 == 0:
				continue
			inter = set.intersection(set(str(x)),set(str(y)))
			if inter is not None and len(inter) == 1:
				#print(x,y)
				#print(inter)

				if len(list(str(x))) == len(set(str(x))):
					xx = set(str(x)) - inter
				else:
					xx = inter
				xx = int(list(xx)[0])
				if len(list(str(y))) == len(set(str(y))):
					yy = set(str(y)) - inter
				else:
					yy = inter
				yy = int(list(yy)[0])
				if xx < yy and x/y == xx/yy:
					print (x,y)
					nontrivial.append((xx,yy))
	print (nontrivial)



