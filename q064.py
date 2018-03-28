import math

class surds:
	#x denotes the rational part of the surd
	#y denotes the irrational part of the surd
	#hence the denotion is like x + sqrt(y)
	#c denotes the denominator if the surd is in a fractional form

	def __init__(self):
		self.x = 0
		self.y = 0
		self.c = 1
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.c = 1

	def __init__ (self,x,y,c):
		self.x = x
		self.y = y
		self.c = c

	def extractInt(self):
		x = 0
		if self.y>0:
			x = int((self.x+math.sqrt(self.y))/self.c)
		else:
			x = int((self.x-math.sqrt(self.y))/self.c)
		xx = self.x - self.c*x
		return (x,surds(xx,self.y,self.c))


	def inverseRationalize(self):
		if self.x>0 and self.y>0:
			self.x = self.x
			self.y = -self.y
			self.c = (self.x**2-abs(self.y))/self.c
		if self.x>0 and self.y<0:
			self.x = self.x
			self.y = -self.y
			self.c = (self.x**2-abs(self.y))/self.c
		if self.x<0 and self.y>0:
			self.x = -self.x
			self.y = self.y
			self.c = (abs(self.y) -self.x**2)/self.c
		if self.x<0 and self.y<0:
			self.x = self.x
			self.y = -self.y
			self.c = (abs(self.y) - self.x**2)/self.c

	def print(self):
		print ('x:',self.x,'y:',self.y,'c:',self.c)

	def __eq__(self,x):
		return self.x == x.x and self.y == x.y and self.c == x.c

	def __ne__(self,x):
		return self.x != x.x or self.y != x.y or self.c != x.c


def genContFracSqrt(n):
	fracs = []
	i = int(math.sqrt(n))
	x = surds(-i,n,1) 
	#x.print()
	fracs.append(i)
	z = surds(x.x,x.y,x.c)
	z.inverseRationalize()
	#z.print()
	count = 5
	#print (z == x)
	while(1):
		(y,z) = z.extractInt()
		#z.print()
		#x.print()
		#print()
		fracs.append(y)
		if (z == x):
			break

		z.inverseRationalize()
		count -= 1

	return fracs

	
if __name__ == '__main__':

	count = 0
	for x in range(2,10001):
		if math.sqrt(x) == int(math.sqrt(x)): continue
		print (x)
		l = genContFracSqrt(x)
		print (l)
		if len(l) % 2 == 0:
			count += 1
		print()

	x = surds(1,2,1)
	y = surds(1.0,2.0,1.0)
	print (y==x)

	

	print (count)