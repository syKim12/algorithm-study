from collections import deque

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    start_x, start_y = 0, 0
    cnt = 1
    q = deque()
    q.append((start_x, start_y, cnt))
    visited[start_x][start_y] = 1
    while q:
        now_x, now_y, now_cnt = q.popleft()
        #print(now_x, now_y)
        if now_x == (N-1) and now_y == (M-1):
            print(now_cnt)
            return
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny, now_cnt+1))
        

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    temp = list(map(int, input()))
    for j in range(M):
        arr[i][j] = temp[j]

visited = [[0]*M for _ in range(N)]
bfs()
