import sys
from heapq import heappop, heappush

def dijkstra(start, graph):
    q = []
    distance = [1e9]*(student+1)
    distance[start] = 0
    heappush(q, (0, start))
    while q:
        dist, num = heappop(q)
        if distance[num] < dist:
            continue
        for i in graph[num]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance


student, route, village = map(int, sys.stdin.readline().split())
graph_departure = [[] for _ in range(student+1)]
graph_arrival = [[] for _ in range(student+1)]
for _ in range(route):
    i, j, v = map(int, sys.stdin.readline().split())
    graph_departure[i].append((j, v))
    graph_arrival[j].append((i, v))
dist_departaure = dijkstra(village, graph_departure)
dist_arrival = dijkstra(village, graph_arrival)
answer = [dist_arrival[i] + dist_departaure[i] for i in range(1, student+1)]
print(max(answer))