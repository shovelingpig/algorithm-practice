import sys
import heapq


input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# O(ElogE) = O(ElogV^2) = O(ElogV)
def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start)) # heap -> compare first element of tuples
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for edge in graph[node]:
            next_node = edge[0]
            edge_weight = edge[1]
            cost = distance[node] + edge_weight # cost = D(start -> node -> next_node)
            if cost < distance[next_node]: # cost < D(start -> next_node)
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])
