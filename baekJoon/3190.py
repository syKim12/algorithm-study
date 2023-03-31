import sys
from collections import deque

def debug(ls):
    for l in ls:
        print(l)
    print("-----------")
    return

def pivot(origin, n_direction):
    if n_direction == 'D':
        return (origin + 1) % 4
    else:
        return ((origin - 1) + 4) % 4

def snake():
    time = 0
    snake = deque()
    snake.append((0, 0))
    direction = 0
    while snake:
        head_x, head_y = snake[-1]
        arr[head_x][head_y] = 1
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]
        time += 1
        # 이동
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 1: # 벽 또는 자기 자신과 부딪힐 때
            break
        elif arr[nx][ny] == 0: # 사과가 없을 때
            remove_x, remove_y = snake.popleft() 
            arr[remove_x][remove_y] = 0
        elif arr[nx][ny] == -1: # 사과가 있을 때
            arr[nx][ny] = 0
        snake.append((nx, ny))
        # 방향 전환
        if len(time_q) > 0:
            if time == time_q[0][0]:
                direction = pivot(direction, time_q[0][1])
                time_q.popleft()
        #debug(arr)        
    return time

N = int(input())
arr = [[0]*N for _ in range(N)]
time_q = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i = int(input())
for _ in range(i):
    r, c = map(int, sys.stdin.readline().split())
    arr[r-1][c-1] = -1 # 사과는 -1로 표시

i = int(input())
for _ in range(i):
    t, direction = sys.stdin.readline().split()
    time_q.append((int(t), direction))

print(snake())    