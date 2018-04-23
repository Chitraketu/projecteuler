import dijkstra
from q082 import addNodeUp,addNodeDown

filename = 'p083_matrix.txt'

def addNodeLeft(mat,adj,cost,i,j):
	x = len(mat)
	if j - 1 >= 0:
		#print (i,j,'right')
		adj[i*x + j + 1].append(i*x + j)
		cost[i*x + j + 1].append(mat[i][j-1])

def addNodeRight(mat,adj,cost,i,j):
	x = len(mat)
	if j + 1 < len(mat):
		#print (i,j,'right')
		adj[i*x + j + 1].append(i*x + j + 2)
		cost[i*x + j + 1].append(mat[i][j+1])


def generateGraph(mat):
	n = len(mat)**2 + 1
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	#print (len(adj))
	# for the first node 
	adj[0].append(1)
	cost[0].append(mat[0][0])

	for i in range(len(mat)):
		for j in range(len(mat)):
			addNodeLeft(mat,adj,cost,i,j)
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



	