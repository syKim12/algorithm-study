from collections import deque
from math import floor
"""
def bfs():
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    start_x, start_y = 0, 0
    calculate = []
    calculate_array = [[0]*n for _ in range(n)]
    q = deque()
    q.append([start_x, start_y])
 
    
    print(array)
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                gap = abs(array[x][y] - array[nx][ny])
                print(x, y, nx, ny, gap)
                if left <= gap <= right:
                    if not calculate_array[x][y]:
                        calculate_array[x][y] = 1
                        calculate.append(array[x][y])
                    calculate_array[nx][ny] = 1
                    visited[nx][ny] = 1
                    calculate.append(array[nx][ny])
                q.append([nx, ny])
    #put values
    print(calculate)
    if len(calculate) > 1:
        avg = floor(sum(calculate)/len(calculate))
        for r in range(n):
            for c in range(n):
                if calculate_array[r][c]:
                    array[r][c] = avg
        cnt = 1
    print("***")
    return cnt
"""

def bfs(i, j):
    cnt = 0
    q = deque()
    move_list = deque()
    q.append((i, j))
    move_list.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                gap = abs(array[x][y] - array[nx][ny])
                if left <= gap <= right:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    move_list.append((nx, ny))           
    return move_list

#set dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#load data and set variable
n, left, right = map(int, input().split())
array = []
cnt = 0
for _ in range(n):
    data = list(map(int, input().split()))
    array.append(data)

while True:
    done = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                move = bfs(i, j)
                if len(move) > 1:    
                    population = sum([array[x][y] for x, y in move]) // len(move)
                    for x, y in move:
                        array[x][y] = population
                    done = 1
    if not done:
        break
    
    cnt += 1

print(cnt)




