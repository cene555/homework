import heapq

def addEdge(adj, u, v, wt):
    adj[u].append((v, wt))
    adj[v].append((u, wt))

def delEdge(adj, u, v, wt):
    for i in range(len(adj[u])):
        if (adj[u][i] == (v, wt)):
            adj[u].pop(i);
            break;

    for i in range(len(adj[v])):
        if (adj[v][i] == (u, wt)):
            adj[v].pop(i);
            break;

def addVertex(adj, vk, u, v, wt):
    addEdge(adj, u, vk, wt)
    addEdge(adj, vk, v, wt)

def delVertex(adj, vertex):
    for key in adj:
        for i in key:
            if i[0] == vertex:
                key.pop(key.index(i))
        


def shortestPath(adj, V, src):
    pq = []

    dist = [float('inf')] * V

    heapq.heappush(pq, (0, src))
    dist[src] = 0

    while pq:
        distance, u = heapq.heappop(pq)

        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    print("Vertex Distance from Source")
    for i in range(V):
        print(i,"   ",dist[i])


V = 9
adj = [[] for _ in range(V)]

addEdge(adj, 0, 1, 4)
addEdge(adj, 0, 7, 8)
addEdge(adj, 1, 2, 8)
addEdge(adj, 1, 7, 11)
addEdge(adj, 2, 3, 7)
addEdge(adj, 2, 8, 2)
addEdge(adj, 2, 5, 4)
addEdge(adj, 3, 4, 9)
addEdge(adj, 3, 5, 14)
addEdge(adj, 4, 5, 10)
addEdge(adj, 5, 6, 2)
addEdge(adj, 6, 7, 1)
addEdge(adj, 6, 8, 6)
addEdge(adj, 7, 8, 7)

print(adj)

print(shortestPath(adj, V, 0))

print('Удаление ребра с началом в 0, концом в 1 и весом 4')
delEdge(adj, 0, 1, 4)
print(adj)

print('Добавление вершины 8')
addVertex(adj, 8, 7, 6, 20)
print(adj)
print('Удаление вершины 7')
delVertex(adj, 7)
print(adj)

