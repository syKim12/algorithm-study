from heapq import heappop, heappush
import sys

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9]*(v+1)

for _ in range(e):
    i, j, w = map(int, sys.stdin.readline().split())
    graph[i].append((j, w))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, v+1):
    if i == start:
        print(0)
    elif distance[i] != 1e9:
        print(distance[i])
    else:
        print('INF')