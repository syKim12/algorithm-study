from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 9)

# 0, 4를 방문하지 않음
def debug(ls):
    print("#############")
    for l in ls:
        print(l)
    return

def bfs():
    global cnt
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q.append((0, 0, visited)) 
    while q:
        x, y, visited = q.popleft()

        # print(x,y)
        if x == N-1 and y == M-1:
            cnt += 1
            # print(q)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                #print(x,y, nx, ny)
                if arr[nx][ny] < arr[x][y]:
                    # print(x,y, nx, ny)
                    temp_visited = deepcopy(visited)
                    temp_visited[nx][ny] = 1
                    q.append((nx,ny, temp_visited))
    return

def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

def main():
    global cnt, N, M, arr, dp, dx, dy
    N, M = map(int, input().split())
    arr = []
    cnt = 0
    dp = [[-1]*M for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(dfs(0,0))    
    return

main()