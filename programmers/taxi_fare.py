"""
import heapq
from collections import deque
def solution(n, s, a, b, fares):
    answer = 0
    INF = 1e9
    distance = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = map(int, fare)
        graph[c].append((d,f))
        graph[d].append((c,f))
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        fare, now = heapq.heappop(q)
        if distance[now] < fare:
            continue
        for i in graph[now]:
            cost = fare + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    print(distance)
    q = deque()
    visited_a = [0]*(n+1)
    visited_b = [0]*(n+1)
    dp_a = [INF]*(n+1)
    dp_b = [INF]*(n+1)
    q.append([s, visited_a, visited_b, dp_a, dp_b])
    while q:
        now, visited_a, visited_b, dp_a, dp_b = q.popleft()
        for i in range(1,n+1):

            if not visited_a[i] and not visited_b[i] and graph

    return answer
"""


def solution(n, s, a, b, fares):
    answer = 0
    INF = 1e9
    #distance = [[INF] * (n + 1) for _ in range(n + 1)]
    graph = [[INF]*(n+1) for _ in range(n + 1)]
    for fare in fares:
        c, d, f = map(int, fare)
        graph[c][d] = f
        graph[d][c] = f
    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # if distance[i][j] > distance[i][k] + distance[k][j]:
                #    distance[i][j] = distance[i][k] + distance[k][j]
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[j][i] = graph[i][j] # 이 부분 없으면 최대 속도 약 2395, 있으면 더 느려짐
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    print(graph)
    return answer
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

"""
#dijkstra code from https://chocochip101.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-%ED%95%A9%EC%8A%B9-%ED%83%9D%EC%8B%9C-%EC%9A%94%EA%B8%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4

import heapq

def solution(n, s, a, b, fares):

    link = [[] for _ in range(n+1)]
    for x, y, z in fares:
        link[x].append((z, y))
        link[y].append((z, x))

    def dijkstra(start):
        dist = [987654321] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # print(dp)
    answer = 987654321
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer
"""