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
    F = deque(fire)
    while F:
        #print(F)
        x_f, y_f = F.popleft()
        fire_visited[x_f][y_f] = 1 
        for i in range(4):
            fx = x_f + dx[i]
            fy = y_f + dy[i]
            #print(fx, fy)
            #debug(fire_visited)
            if 0 <= fx < r and 0 <= fy < c and not fire_visited[fx][fy]:
                if arr[fx][fy] == '.' or arr[fx][fy] == '$':
                    arr[fx][fy] = 'F'
                    fire.append((fx, fy))
    F = deque(fire)  
           
    

def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    time = 0
    while True:
        time += 1
        bfs_fire()
        while q:
            temp_j = []
            x, y = q.popleft()
            if x == 0 or x == r - 1 or y == 0 or y == c - 1:
                #debug(arr)
                return time
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] == '.':
                    arr[x][y] = '$'
                    arr[nx][ny] = 'J'
                    temp_j.append((nx, ny))
        #debug(arr)    
        q = deque(temp_j)    
        if not q:    
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