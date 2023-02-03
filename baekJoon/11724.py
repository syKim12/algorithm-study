import sys
from collections import deque

def bfs(i):
    #print("--------")
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        x = q.popleft()
        for y in range(1, N+1): # range(x, N+1)로 둘 경우 테스트 케이스에 걸린다. 
            #print(x, y)
            if arr[x][y] == 0 and visited[y] == 0:
                arr[x][y], arr[y][x] = 1, 1
                visited[y] = 1
                q.append(y)
    return

N, M = map(int, sys.stdin.readline().split())
arr = [[-1]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i][j], arr[j][i] = 0, 0

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)