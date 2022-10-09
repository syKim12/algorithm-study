# make a combination, then calculate
from itertools import combinations
from collections import deque
from copy import deepcopy


n, m = map(int, input().split())
wall, virus, blank = [], [], []
array = [[0]*m for _ in range(n)]
max_block = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a):
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for v in virus:
        x, y = v[0], v[1]
        visited[x][y] = 1
        q = deque()
        q.append([x,y])
        while q:
            now_x, now_y = q.popleft()
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny] and a[nx][ny] == 0:
                    a[nx][ny] = 2
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    for r in range(n):
        for c in range(m):
            if a[r][c] == 0:
                cnt += 1
    return cnt


for r in range(n):
    data = list(map(int, input().split()))
    for c in range(m):
        if data[c] == 1:
            array[r][c] = 1
            wall.append((r, c))
        elif data[c] == 2:
            array[r][c] = 2
            virus.append((r, c))
        else:
            array[r][c] = 0
            blank.append((r, c))

candidates = combinations(blank, 3)

for candidate in candidates:
    new_array = deepcopy(array)
    #print(new_array)
    for c in candidate:
        x, y = c[0], c[1]
        new_array[x][y] = 1
    block = bfs(new_array)    
    if block > max_block:
        max_block = block


print(max_block)
    