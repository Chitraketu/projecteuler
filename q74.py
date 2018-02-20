from math import factorial as f
import functools

def sumOfDigitFact(n):
	return sum(map(lambda x:f(int(x)),list(str(n))))

if __name__ == '__main__':
	n = 10**6
	count = 0
	for x in range(1,n):
		l = set()
		sfd = sumOfDigitFact(x)
		while(not sfd in l):
			l.add(sfd)
			sfd = sumOfDigitFact(sfd)
		if len(l) == 59:
			count += 1
			print (x)

	print (count)
