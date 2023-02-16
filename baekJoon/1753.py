from heapq import heappop, heappush

v, e = map(int, input().split())
start = int(input())
arr = [[1e9]*(v+1) for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    arr[u][v] = min(arr[u][v], w)