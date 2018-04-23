import dijkstra

filename = 'p082_matrix.txt'

def addNodeUp(mat,adj,cost,i,j):
	x = len(mat)
	if i - 1 >= 0:
		#print (i,j,'up')
		adj[i*x + j + 1].append((i-1)*x + j + 1)
		cost[i*x + j + 1].append(mat[i-1][j])

def addNodeDown(mat,adj,cost,i,j):
	x = len(mat)
	if i + 1 < len(mat):
		#print (i,j,'down')
		adj[i*x + j + 1].append((i+1)*x + j + 1)
		cost[i*x + j + 1].append(mat[i+1][j])

def addNodeRight(mat,adj,cost,i,j):
	x = len(mat)
	if j + 1 < len(mat):
		#print (i,j,'right')
		adj[i*x + j + 1].append(i*x + j + 2)
		cost[i*x + j + 1].append(mat[i][j+1])
	if j + 1 == len(mat):
		#print (i,j,'right')
		adj[i*x + j + 1].append(len(adj)-1)
		cost[i*x + j + 1].append(0)

def generateGraph(mat):
	n = len(mat)**2 + 2
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	#print (len(adj))
	# for the first node 
	ind = 0
	for i in range(len(mat)):
		adj[0].append(ind+1)
		cost[0].append(mat[i][0])
		ind += len(mat)
	#print (adj[0])
	for i in range(len(mat)):
		for j in range(len(mat)):
			addNodeRight(mat,adj,cost,i,j)
			addNodeDown(mat,adj,cost,i,j)
			addNodeUp(mat,adj,cost,i,j)
	return (adj,cost)

if __name__ == '__main__':
	l = []
	with open(filename,'r')	as f:
		for line in f:
			l.append(list(map(int,line.rstrip().split(','))))
	length = len(l)
	#l = [list(i) for i in zip(*l)]
	#for x in l:
		#print (x)
	(adj,cost) = generateGraph(l)
	'''
	print ()
	for x in l:
		print (x)
	print ()
	for i,x in enumerate(adj):
		print (i,x)
	print ()
	for i,x in enumerate(cost):
		print (i,x)

	'''
	(s,t) = (0,len(adj)-1)
	print(dijkstra.distance(adj, cost, s, t))



	