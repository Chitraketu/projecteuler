
filename = "p079_keylog.txt"

def topSortUtil(node,visited,stack,adj):
	visited[node] = True
	for i in adj[node]:
		if visited[i] == False:
			topSortUtil(i,visited,stack,adj)

	stack.insert(0,node) 

def topological(adj,nodes):
	visited = {}
	for x in nodes:
		visited[x] = False
	stack = []
	for i in range(len(nodes)):
		if visited[nodes[i]] == False:
			topSortUtil(nodes[i],visited,stack,adj)
	return stack

if __name__ == '__main__':
	l = []
	with open(filename,"r") as f:
		l = f.read().splitlines()
	adj = {}
	for x in l:
		sl = list(map(int,list(x)))	
		(a,b,c) = sl
		if a in adj:
			adj[a].extend([b,c])
		else:
			adj[a] = [b,c]

		if b in adj:
			adj[b].append(c)
		else:
			adj[b] = [c]

	nodes = set()

	for x in adj:
		nodes.add(x)
		for ed in adj[x]:
			nodes.add(ed)
		adj[x] = set(adj[x])
		print (x,':',adj[x])

	for x in nodes:
		if x not in adj:
			adj[x] = {}

	print (''.join(list(map(str,(topological(adj,list(nodes)))))))