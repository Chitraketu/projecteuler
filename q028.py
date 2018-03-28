#diagonal sum

def findSumDiagonal(n):
	i = 3
	s = 1
	k = 0
	inc = 2
	while(i <= n**2):
		print (i)
		print (inc)
		print (k)
		print ()
		s += i
		if k == 3:
			k = 0
			inc += 2
		else:
			k += 1
		i += inc
	return s


if __name__ == "__main__":
	n = int(input())
	print (findSumDiagonal(n))
