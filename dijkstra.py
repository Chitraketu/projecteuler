#Uses python3

'''
This is a python script which calculates the shortest path using Dijkstra's algorithm. It is implemented
using Min-Heap for the performance optimization purpose. 
This algorithm's time complexity is O(|V| + |E|)*log(|V|)
whereas it requires an extra memory of O(|V|^2)
'''


import sys
import queue




# code for the heap operations
# variables for building the heap
# the heap is always a complete tree
size = 0
H = []
maxSize = 0
inf = 2 ** 128 - 1


#returns the parent of the index in the heap
def parent(i):
    return int((i - 1) / 2)


#returns the left child of the index in the heap
def leftChild(i):
    return 2 * i + 1


#returns the right child of the index in the heap
def rightChild(i):
    return 2 * i + 2


#tries to sift the value upward in the binary heap if it has less weight since
# this is a min heap
def siftUp(i):
    global H
    while i > 0 and H[parent(i)][1] > H[i][1]:
        (H[parent(i)], H[i]) = (H[i], H[parent(i)])
        i = parent(i)

#tries to sift the value downward in the binary heap if it has more weight
def siftDown(i):
    global H
    maxIndex = i
    l = leftChild(i)
    if l < size and H[l][1] < H[maxIndex][1]:
        maxIndex = l
    r = rightChild(i)
    if r < size and H[r][1] < H[maxIndex][1]:
        maxIndex = r

    if not i == maxIndex:
        (H[i], H[maxIndex]) = (H[maxIndex], H[i])
        siftDown(maxIndex)


#this inserts the value in the heap
def insert(p, dist):
    global H
    global size
    if size == maxSize:
        pass
    size = size + 1
    H[size] = (p, dist)
    siftUp(size)


# extracts the minimum value from the heap
def extractMin():
    global H
    global size
    result = H[0]
    H[0] = H[size - 1]
    size = size - 1
    siftDown(0)
    return result[0]


# removes the certain element from the heap and then again adjusts the minimum value of all the heap data
def remove(i):
    global H
    H[i] = (H[i][0], inf)
    siftUp(i)
    extractMax()


# changes the priority of certain value of the heap and then again adjusts its position in heap according to its new weight
def changePriority(i, p, dist):
    global H
    oldP = H[i]
    H[i] = (p, dist)
    if dist > oldP[1]:
        siftDown(i)
    else:
        siftUp(i)


# builds the heap form an unordered array of tuples
def buildHeap():
    global H
    global size
    global maxSize
    size = len(H)
    maxSize = len(H)
    for i in range(int(len(H) / 2), -1, -1):
        siftDown(i)

#finds the index of the element in the heap
def findIndex(v, H):
    for (x, y) in enumerate(H):
        if y[0] == v:
            return x
    return -1

#code for the heap finished



# implementation of the dijkstra's algorithm using the min heap as a priority queue
# the runtimme of this algorithm is O((|V|+|E|)log(|V|)
# which comes as follows: extracting the minimum from the heap and then changing the priority takes log|V| operation and 
# this is done for V times and E times
def distance(adj,cost,s,t):
    global H
    global size
    size = 0
    H = []
    maxSize = 0

    dist = {}
    prev = {}
    for (i, v) in enumerate(adj):
        dist[i] = inf
        prev[i] = -1
    dist[s] = 0
    H.clear()
    #print(H)
    for i,v in enumerate(dist):
        H.append((i,dist[v]))
    
    buildHeap()    
    while not size == 0:
        u = extractMin()
        for i,v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                ind = findIndex(v, H)
                if not ind == -1:
                    changePriority(ind, v, dist[v])

    if dist[t] == inf:
    	result = -1
    else:
    	result = dist[t]
    return result


def distanceAll(adj,cost,s):
    global H
    global size
    size = 0
    H = []
    maxSize = 0

    dist = {}
    prev = {}
    for (i, v) in enumerate(adj):
        dist[i] = inf
        prev[i] = -1
    dist[s] = 0
    H.clear()
    #print(H)
    for i,v in enumerate(dist):
        H.append((i,dist[v]))
    
    buildHeap()    
    while not size == 0:
        u = extractMin()
        for i,v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                ind = findIndex(v, H)
                if not ind == -1:
                    changePriority(ind, v, dist[v])

    return dist






'''
input is taken in the format 
n,m -> number of vertices and edges
u,v,w -> directed edge (u,v) with weight w in m lines
s,t -> source and destination
output is given as the minimum weight
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    (n, m) = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:3 * m:3], data[1:3 * m:3]), data[2:3
                 * m:3]))
    data = data[3 * m:]

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    (s, t) = (data[0] - 1, data[1] - 1)
    if len(edges) == 0:
    	if s == t:
    		print(0)
    	else:
    		print(-1)
    else:
    	print(distance(adj, cost, s, t))
			