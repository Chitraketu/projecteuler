from fractions import Fraction as f

def convergent(list):
	s = 0
	for x in range(len(list)-1,-1,-1):
		print (x)	
		if x == len(list) - 1:
			s = s + f(1,list[x])
			print (s)
		else:
			s = s + list[x]
			s = 1/s
			print (s)
	return 1/s

if __name__ == '__main__':
	e_list = [2]
	count = 1
	k = 2
	while (count <= 100):
		e_list.extend([1,k,1])
		k += 2
		count +=3
	e_list = e_list[:100]
	print (e_list)
	print (len(e_list))
	numerator = convergent(e_list).numerator
	s = sum(list(map(int,str(numerator))))
	print (s)
