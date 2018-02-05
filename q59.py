import sys
filename = 'p059_cipher.txt'

def isAlphabet(xx):
	x = ord(xx)
	symbols = ['.','?',',',';',':','-','(',')','[',']','{','}','\'','"','!','/', ' ','0','1','2','3','4','5','6','7','8','9']
	ascii_symbols = list(map(ord,symbols))
	return ord('A') <= x <= ord('Z') or ord('a') <= x <= ord('z') or xx in symbols

def encode(s,l):
	encoded = []
	for i in range(len(s)):
		encoded.append(chr(ord(s[i]) ^ ord(l[i%len(l)])))
	return encoded

def isDecipherable(s,l):
	enc = encode(s,l)
	msg = ''
	for x in enc:
		if not isAlphabet(x):
			return ''
		else:
			msg += x
	return msg


if __name__ == '__main__':

	with open(filename,'r') as r:
		c = r.read().splitlines()
	c = c[0].split(',')
	c = list(map(int,c))
	c = list(map(chr,c))

	strin = 'hello world'
	key = 'abc'

	encoded = encode(strin,key)
	#c = encoded
	print (c)

	a = ord('a')
	print (a)
	print (isAlphabet('a'))
	for x in range(26):
		for y in range(26):
			for z in range(26):
				(xx,yy,zz) = (x+a,y+a,z+a)
				#print (xx,yy,zz)
				ch = chr(xx)+chr(yy)+chr(zz)
				print (ch)
				r = isDecipherable(c,ch)
				if len(r):
					print (r)
					s = sum(map(ord,r))
					print (s)
					sys.exit()
	#print (c)
	print (len(c))
	d = list(map(chr,c))
	print (d)