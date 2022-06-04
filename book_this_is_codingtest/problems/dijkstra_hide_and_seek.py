import heapq
import sys
input = sys.stdin.readline
INF = 1e9
#노드 n개, 간선 m개
n, m = map(int, input().split())
# 각 노드 연결된 노드 정보 담는 리스트
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 cost는 1, 양방향
    graph[a].append((b, 1))
    graph[b].append((a,1))

q = []
start = 1
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        #현재 노드를 거쳐 다른 노드로 갈 때 값이 더 작은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
#최대값을 가지는 가장 작은 노드 번호를 구하기 위해 초기 셋팅
max_node = 0
max_distance = 0
result = []
for i in range(1, n+1):
    if distance[i] > max_distance:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif distance[i] == max_distance:
        result.append(i)

print(max_node, max_distance, len(result))