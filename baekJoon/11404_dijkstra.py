import sys
from heapq import heappop, heappush

def dijkstra(start, end):
    distance = [1e9]*(city+1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            val = dist + i[1]
            if val < distance[i[0]]:
                distance[i[0]] = val
                heappush(q, (val, i[0]))
    return distance[end]

city = int(input())
edge = int(input())
graph = [[] for _ in range(city+1)]

for _ in range(edge):
    i, j, c = map(int, sys.stdin.readline().split())
    graph[i].append((j, c))

for i in range(1, city+1):
    for j in range(1, city+1):
        print(dijkstra(i, j), end=' ')
    print('\n')