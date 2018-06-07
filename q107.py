
filename = 'p107_network.txt'

'''
code for the disjoint set datastructure
'''
def makeSet(i,parent,rank):
    parent[i] = i
    rank[i] = 0

def find(i,parent,rank):
    if i != parent[i]:
        parent[i] = find(parent[i],parent,rank)
    return parent[i]

def union(i,j,parent,rank):
    i_id = find(i,parent,rank)
    j_id = find(j,parent,rank)
    if i_id == j_id:
        return False
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1
    return True

''' kruskals algorithm'''
def minSpan(x,adj):
	parent = {}
	rank = {}
	result = 0
	sortAdj = sorted(adj,key=adj.get)
	for i,v in enumerate(x):
		makeSet(i,parent,rank)
	for j in sortAdj:
		if union(j[0],j[1],parent,rank):
			result += adj[j]
	return result


if __name__ == '__main__':
	l = []
	with open(filename,'r')	as f:
		for line in f:
			l.append(line.rstrip().split(','))
	s = 0
	for i in range(len(l)):
		for j in range((len(l[i]))):
			if l[i][j] == '-':
				l[i][j] = 999999
			else:
				s += int(l[i][j])
			l[i][j] = int(l[i][j])
	adj = {}
	for i in range(len(l)):
		for j in range(i+1,len(l[i])):
			adj[(i,j)] = l[i][j]

	print (l)
	print (s//2 - minSpan(list(range(40)),adj))