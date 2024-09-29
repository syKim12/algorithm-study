import sys
from collections import deque

def destroy(dir, distance, x, y):
    for _ in range(distance):
        x += sx[dir]
        y += sy[dir]
        if x < 0 or x >= N or y < 0 or y >= N:
            return
        arr[x][y] = 0
    return

def move():
    for i in range(len(path)):
        x,y = path[i]
        if arr[x][y] == 0:
            flag = 1
            for j in range(i, len(path)):
                value = arr[path[j][0]][path[j][1]]
                if  value > 0:
                    flag = 0
                    arr[x][y] = value
                    arr[path[j][0]][path[j][1]] = 0
                    break
            if flag:
                return
    return

def explode():
    global point
    num = arr[path[0][0]][path[0][1]]
    cnt = 1
    explosion = []
    temp = [path[0]] # 이동 경로
    for i in range(1, len(path)):
        #if arr[path[i][0]][path[i][1]] == 0:
        #    break
        #print(path[i], num, arr[path[i][0]][path[i][1]], temp, cnt)
        if arr[path[i][0]][path[i][1]] == num:
            cnt += 1
            temp.append(path[i]) # 이동경로에 추가
        else:
            if cnt >= 4: # 값이 달라졌으므로 이 때까지 이동한 경로중 구슬 4개 이상이면 폭발 리스트에 추가
                explosion += temp
                point += num * cnt
            # 값 초기화
            cnt = 1
            num = arr[path[i][0]][path[i][1]]
            temp = [path[i]]
    #print(explosion)
    if len(explosion) == 0:
        return 0
    for x, y in explosion:
        arr[x][y] = 0
    return 1

def change():
    cnt = 1
    num = arr[path[0][0]][path[0][1]]
    fill = []
    for i in range(1,len(path)):
        x,y = path[i]
        if arr[x][y] == num:
            cnt += 1
        else:
            fill += [cnt, num]
            # 값 초기화
            num = arr[x][y]
            cnt = 1
    if len(fill) > 0:
        for i in range(len(fill)):
            if i >= len(path): # 구슬이 칸의 수보다 많을 때
                return
            fx, fy = path[i]
            arr[fx][fy] = fill[i]
    return



N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

sx = [-1, 1, 0, 0]
sy = [0, 0, -1, 1]
# 이동 경ㄹ
x, y = N//2, N//2
dir = 0
path = []
break_flag = 0
for num in range(1, N+1):
    for _ in range(2):
        for _ in range(num):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx == 0 and ny == 0:
                break_flag = 1
                path.append((0,0))
                break
            if 0 <= nx < N and 0 <= ny < N:
                path.append((nx, ny))
                x, y = nx, ny
        dir += 1
        dir = dir % 4
        if break_flag:
            break
    if break_flag:
        break
point = 0
for _ in range(M):
    dir, distance = map(int, input().split())
    destroy(dir-1, distance, N//2, N//2)
    move()
    while explode(): # 폭발할 구슬이 없을 때까지 반복
        move()
    change()
    #print((arr))
print(point)