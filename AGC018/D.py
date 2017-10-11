def search_child(v):
	return search_child()

N = int(input())
temp = [ input() for _ in range(N-1) ]
edge = [None]*(N-1)
adj = []
for i in range(N+1):
	adj.append([])

for i in range(N-1):
	abc = list(map(int,temp[i].split(" ")))
	edge[i] = [abc[0], abc[1], abc[2]]
	adj[abc[0]].append([abc[1],abc[2]])
	adj[abc[1]].append([abc[0],abc[2]])
###########################################
#重心探索
for i in range(1,N+1):
	if len(adj[i]) != 1:
		for child in adj[i]:
			adj[child[0]]
		print(adj[i])