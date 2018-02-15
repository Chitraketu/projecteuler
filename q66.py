import math
import q64
from fractions import Fraction as f

def pells(x,y,d):
	return x**2 - d*y*y == 1.0

if __name__ == '__main__':


	maxd = 0
	maxx = 0
	for d in range(2,1001):
		if math.sqrt(d) == int(math.sqrt(d)): continue
		conFrac = q64.genContFracSqrt(d)
		a = conFrac[0]
		conFrac = conFrac[1:]
		#print (d,conFrac)
		l = 1
		while(1):
			ll = len(conFrac)
			frac = f(1,conFrac[(l-1)%ll])
			#print ("frac",frac)
			for x in range(l-1,0,-1):
				frac = 1 / (conFrac[(x-1)%ll] + frac)
				#print ("frac",frac)

			frac = a + frac
			#print ("frac:",frac)
			x = frac.numerator
			y = frac.denominator

			if pells(x,y,d):
				if maxx < x:
					print (x,y,d)
					maxx = x
					maxd = d
				break

			l += 1
	print (maxd)



