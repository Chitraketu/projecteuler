
filename = 'p054_poker.txt'

cards = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
def sameSuite(arr):
	global cards
	s = arr[0][1]
	for x in arr:
		if x[1] != s:
			return False

	return True

def royalFlush(arr):
	global cards
	royal = cards[8:len(cards)]
	if not sameSuite(arr):
		return False

	for x in arr:
		if not x in royal:
			return False
	return True

def straightFlush(arr):
	if not sameSuite(arr):
		return False
	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	#print (arr)
	r = [cardsval[x[0]] for x in arr]
	r.sort()
	return len(r) == (int(r[len(r)-1]) - int(r[0]))

def xOfKind(arr,xx):
	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	#print (arr)
	r = [cardsval[x[0]] for x in arr]
	r.sort()
	d = {}
	for x in r:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1

	for x in d:
		if d[x] == xx:
			return True

	return False

def xOfKindVal(arr,xx):
	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	#print (arr)
	r = [cardsval[x[0]] for x in arr]
	r.sort()
	d = {}
	for x in r:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1

	for x in d:
		if d[x] == xx:
			return x

	return -1


def fourOfAKind(arr):
	return xOfKind(arr,4)

def fullHouse(arr):
	return xOfKind(arr,3) and xOfKind(arr,2)

def flush(arr):
	return sameSuite(arr)

def straight(arr):
	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	#print (arr)
	r = [cardsval[x[0]] for x in arr]
	r.sort()
	return len(r) == (int(r[len(r)-1]) - int(r[0]))

def threeOfAKind(arr):
	return xOfKind(arr,3)

def twoPairs(arr):
	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	#print (arr)
	r = [cardsval[x[0]] for x in arr]
	r.sort()
	d = {}
	for x in r:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1

	count = 0
	for x in d:
		if d[x] == 2:
			count += 1

	return count == 2

def onePair(arr):
	return xOfKind(arr,2)

def highestXofKind(arr1,arr2,x):
	a1 = xOfKindVal(arr1,x)
	a2 = xOfKindVal(arr2,x)
	if a1 > a2:
		return 1
	elif a1 < a2:
		return 2
	else:
		return -1


def highestCard(arr1,arr2):
	r1 = [x[0] for x in arr1]
	r2 = [x[0] for x in arr2]

	global cards
	cardsval = {str(key):i for i,key in enumerate(cards) }
	r1.sort(key=lambda x:cardsval[x],reverse=True)
	r2.sort(key=lambda x:cardsval[x],reverse=True)
	print ('r1',r1)
	print ('r2',r2)
	for i in range(len(r1)):
		#print (r1[i],r2[i])
		if cardsval[r1[i]] > cardsval[r2[i]]:
			return 1
		elif cardsval[r1[i]] < cardsval[r2[i]]:
			return 2


def winner(arr1,arr2):

	print (arr1)
	print (arr2)

	#check for royal flush
	if(royalFlush(arr1) and not royalFlush(arr2)):
		return 1
	if(not royalFlush(arr1) and royalFlush(arr2)):
		return 2
	print('royal flush check finished')

	# check for straight flush
	if(straightFlush(arr1) and not straightFlush(arr2)):
		return 1
	if(not straightFlush(arr1) and straightFlush(arr2)):
		return 2
	print('straight flush check finished')

	# check for four of a kind
	if(fourOfAKind(arr1) and not fourOfAKind(arr2)):
		return 1
	if(not fourOfAKind(arr1) and fourOfAKind(arr2)):
		return 2
	if(fourOfAKind(arr1) and fourOfAKind(arr2)):
		if highestXofKind(arr1,arr2,4) > -1:
			return highestXofKind(arr1,arr2,4)
	print('four of a kind check finished')


	#check for flush
	if(flush(arr1) and not flush(arr2)):
		return 1
	if(not flush(arr1) and flush(arr2)):
		return 2
	if(flush(arr1) and flush(arr2)):
		if highestXofKind(arr1,arr2,3) > -1:
			return highestXofKind(arr1,arr2,3)
		elif highestXofKind(arr1,arr2,2) > -1:
			return highestXofKind(arr1,arr2,2)

	print('flush check finished')


	#check for straight
	if(straight(arr1) and not straight(arr2)):
		return 1
	if(not straight(arr1) and straight(arr2)):
		return 2
	print('straight check finished')

	#check for three of a kind
	if(threeOfAKind(arr1) and not threeOfAKind(arr2)):
		return 1
	if(not threeOfAKind(arr1) and threeOfAKind(arr2)):
		return 2
	if(threeOfAKind(arr1) and threeOfAKind(arr2)):
		if highestXofKind(arr1,arr2,3) > -1:
			return highestXofKind(arr1,arr2,3)
		elif highestXofKind(arr1,arr2,2) > -1:
			return highestXofKind(arr1,arr2,2)

	print('three of a kind check finished')


	#check for two pairs
	if(twoPairs(arr1) and not twoPairs(arr2)):
		return 1
	if(not twoPairs(arr1) and twoPairs(arr2)):
		return 2
	if(twoPairs(arr1) and twoPairs(arr2)):
		if checkHighestTwoPairs(arr1,arr2) > -1:
			checkHighestTwoPairs(arr1,arr2)

	print('two pairs check finished')


	#check for one pair
	if(onePair(arr1) and not onePair(arr2)):
		return 1
	if(not onePair(arr1) and onePair(arr2)):
		return 2

	print('one pair check finished')


	return highestCard(arr1,arr2)















if __name__ == '__main__':
	count1 = 0
	plays = []
	with open(filename,'r') as r:
		plays = r.read().splitlines()
	for i,x in enumerate(plays):
		plays[i] = [plays[i].split(' ')[:5],plays[i].split(' ')[5:]]

	for x in plays:
		win = winner(x[0],x[1])
		print (win)
		if win == 1:
			count1 += 1

		#if count1 == 5:
		#	break
		print ()

	print (count1)



