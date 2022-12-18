import heapq
import sys

def dijkstra(start):
    q = []
    heqpq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if ocst < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, paths, gates, summits):
    answer = []
    INF = 1e9
    graph = [[] for i in range(n+1)]
    distance = [INF]*(n+1)

    for i in range(len(paths)):
        x, y, z = paths[i]
        graph[x].append((y, z))

    for k in gates:
        dijkstra(k)
        count = 0
        max_distance = 0
        for i in range(1, n+1):
            if distance[i] != INF:
                max_distance = max(max_distance, distance[i])


    return answer