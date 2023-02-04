import sys
from collections import deque
import copy

def dfs(i, array, visited):
    visited[i] = 1
    print(i, end=' ')
    for x in range(1, N+1):
        if array[i][x] == 0 and not visited[x]:
            array[i][x], array[x][i] = 1, 1
            dfs(x, array, visited)
    return

def bfs(i, array):
    visited = [0]*(N+1)
    q = deque()
    q.append(i)
    visited[i] = 1
    print(i, end=' ')
    while q:
        x = q.popleft()
        for y in range(1, N+1):
            if array[x][y] == 0 and not visited[y]:
                visited[y] = 1
                array[x][y], array[y][x] = 1, 1
                q.append(y)
                print(y, end=' ')
    return

# get values
N, M, V = map(int, sys.stdin.readline().split())
arr = [[-1]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i][j], arr[j][i] = 0, 0

# dfs
arr_dfs = copy.deepcopy(arr)
dfs(V, arr_dfs, [0]*(N+1))
print("")
# bfs
arr_bfs = copy.deepcopy(arr)
bfs(V, arr_bfs)

