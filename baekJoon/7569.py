import sys
from collections import deque

def bfs(tomato, empty):
    dx = [0, -1, 0, 1, 0, 0]
    dy = [1, 0, -1, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque(tomato) # deque([(m, n, h, days)])
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    while q:
        z, x, y, days = q.popleft()
        visited[z][x][y] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and not visited[nz][nx][ny] and arr[nz][nx][ny] == 0:
                visited[nz][nx][ny] = 1
                arr[nz][nx][ny] = 1
                q.append((nz, nx, ny, days+1))
    # 모두 익지 못하는 상황
    q_empty = deque(empty)
    while q_empty:
        z, x, y = q_empty.popleft()
        if arr[z][x][y] == 0:
            print(-1)
            return
    print(days)    
    return


M, N, H = map(int, input().split())

arr = [[[0]*M for _ in range(N)] for _ in range(H)]
tomato, empty = [], [] # tomato: 토마토가 있는 리스트, empty: 아무것도 없는 리스트
for i in range(H):
    for j in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        for k in range(M):
            temp_value = temp[k]
            arr[i][j][k] = temp_value
            if temp_value == 1:
                tomato.append((i, j, k, 0))
            elif temp_value == 0:
                empty.append((i, j, k))
bfs(tomato, empty)
