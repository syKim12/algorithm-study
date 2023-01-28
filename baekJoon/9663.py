from collections import deque

N = int(input())
cnt = 0
visited = [[0]*N for _ in range(N)]
def bfs(path_list):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]
    visited_bfs = [[0]*N for _ in range(N)]
    # 현재 퀸 위치 표시
    arr = [[0]*N for _ in range(N)]
    for x, y in path_list:
        arr[x][y] = 1
    q = deque()
    q.append(path_list[0])
    while q:
        x, y = q.popleft()
        visited_bfs[x][y] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited_bfs[nx][ny] == 0:
                if arr[nx][ny] == 1: #퀸이 이동할 때 마주치는 경우
                    return 0
    return 1

def sol(N, path_list, idx):
    global cnt
    if idx == N:
        cnt += bfs(path_list)
        return
    for i in range(N):
        for j in range(i, N):
            if not visited[i][j]:
                visited[i][j] = 1
                path_list.append((i, j))
                sol(N, path_list, idx + 1)
                path_list.pop()
                visited[i][j] = 0

sol(N, [], 0)
print(cnt)