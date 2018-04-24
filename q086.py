
if __name__ == '__main__':
	M = 1818 # this is the answer use bisection method to reach here manually
	s2 = []
	print ()
	for i in range(1,2*M+1):
		for j in range(i,2*M+1):
			h = (i**2 + j **2) ** (1.0/2)
			if h == int(h):
				#print (i,j,'count')
				for ii in range(1,i//2+1):
					#print (ii,i-ii,j,'this')
					if max(ii,i-ii) <= j and j <= M:
						#print (ii,i-ii,j,'this added')
						l.append((ii,i-ii,j))
						s2.append((ii,i-ii,j))
				for jj in range(1,j//2+1):
					#print (jj,j-jj,i,'that')
					if max(jj,j-jj) <= i and i <= M:
						#print (jj,j-jj,i,'that added')
						l.append((jj,j-jj,i))	
						s2.append((jj,j-jj,i))	
	print (len(s2))
