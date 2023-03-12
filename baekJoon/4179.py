from collections import deque
import sys

def debug(ls):
    for l in ls:
        print(l)
    print('-----------------')

def bfs_fire():
    global fire
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    length = len(fire)
    for k in range(length):
        x, y = fire[k][0], fire[k][1]
        fire_visited[x][y] = 1 
        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]
            if 0 <= fx < r and 0 <= fy < c and not fire_visited[fx][fy]:
                if arr[fx][fy] == '.':
                    arr[fx][fy] = 'F'
                    fire.append((fx, fy))
                elif arr[fx][fy] == 'J':
                    arr[fx][fy] = 'F'
                    return
    
    #print('----fire-----')
    #debug(arr)
    

def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    time = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return time+1
            elif not visited[nx][ny] and arr[nx][ny] == '.':
                arr[x][y] = '.'
                arr[nx][ny] = 'J'
                q.append((nx, ny))
        bfs_fire()
        time += 1
        #debug(arr)
    return 'IMPOSSIBLE'

r, c = map(int, input().split())
arr = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
fire_visited = [[0]*c for _ in range(r)]
fire = []

for i in range(r):
    temp = sys.stdin.readline()
    for j in range(c):
        if temp[j] == 'J':
            start_r, start_c = i, j
        elif temp[j] == 'F':
            fire.append((i, j))
        elif temp[j] == '#': # 벽도 갈 수 없으므로 visited로 표시
            visited[i][j] = 1
        arr[i][j] = temp[j]

print(bfs(start_r, start_c))