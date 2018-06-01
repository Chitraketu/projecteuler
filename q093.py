from itertools import combinations as cmb
from itertools import permutations as perm
from itertools import product
def eval(a,b,opr):
	if opr == '+':
		return a+b
	elif opr == '-':
		return a-b
	elif opr == '*':
		return a*b
	elif opr == '/':
		try:
			temp_var = a/b
		except ZeroDivisionError:
			temp_var = 0
		return temp_var

def evaluateAll(expr,low,high):
	res = set()
	if low == high:
		res.add(int(expr[low]))
		return res
	if low == high - 2:
		res.add(eval(int(expr[low]),int(expr[high]),expr[low+1]))

	for i in range(low+1,high+1,2):
		l = evaluateAll(expr,low,i-1)
		r = evaluateAll(expr,i+1,high)
		for j in l:
			for k in r:
				res.add(eval(j,k,expr[i])) 
	return res

def getExpr(perm,opr):
	s = ''
	for i in range(len(perm)):
		s += str(perm[i])
		if not i == len(perm)-1:
			s += opr[i]
	return s

def sumOfN(n):
	return n * (n + 1 ) // 2

if __name__ == '__main__':
	digits = list(range(1,9))
	operators = ['+','-','*','/']
	digits_perm = list(cmb(digits,4))
	operators_perm = list(product(operators,repeat=3))
	print (len(operators_perm))
	print (len(digits_perm))
	maxS = 0
	maxEval = ''
	for digitL in digits_perm:
		totalEval = set()
		for pdl in list(perm(digitL)):
			for opr in operators_perm:
				expr = getExpr(pdl,opr)
				evalL = evaluateAll(expr,0,len(expr)-1)
				evalL = set(filter(lambda x: x>0 and int(x) == x,list(evalL)))
				totalEval = totalEval.union(evalL)
		if (digitL == (1,2,3,4)):
			print (totalEval)

		ll = len(totalEval)
		ns = set(range(1,len(totalEval)+1))
		diff = ns.difference(totalEval)
		if maxS < min(diff):
			maxS = min(diff)
			print(totalEval)
			maxEval = digitL

	print (maxEval)
