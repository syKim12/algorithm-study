from collections import deque
import sys

def dfs(src, trgt, dist, min_dist):
    global graph

    print(src, trgt, dist, min_dist)
    for t, d in graph[src]:
  
        min_dist = min(min_dist, dfs(t, trgt, dist+d, min_dist))
        if t == trgt:
            return min_dist 
    return min_dist


def bfs(src, trgt):
    global N
    q = deque()
    visited = [0]*N


def main():
    global graph, N
    sys.stdin = open('1504_test.txt', 'r')
    N, E = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a-1].append((b-1,c))
    v1, v2 = map(int, input().split())
    result = dfs(v1, v2, 0, 1e9)
    print(result)

main()
