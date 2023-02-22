import sys

def dfs(path, cnt):
    global max_cnt, dx, dy, board
    x, y = path[0], path[1]
    max_cnt = max(cnt, max_cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and not alphabet[board[nx][ny]]:        
            visited[nx][ny] = 1
            alphabet[board[nx][ny]] = 1
            dfs((nx, ny), cnt+1)
            #print(nx, ny)
            visited[nx][ny] = 0
            #print(alphabet)
            alphabet[board[nx][ny]] = 0
    return max_cnt

R, C = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, sys.stdin.readline())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*C for _ in range(R)]
alphabet = [0]*26
max_cnt = 0

alphabet[board[0][0]] = 1
visited[0][0] = 1
dfs((0, 0), 1)
print(max_cnt)

