from collections import deque
import sys
from copy import deepcopy

def debug(ls):
    print("###############")
    for l in ls:
        print(l)

def move_dice(dice, dir):
    temp_dice = deepcopy(dice)
    if dir == 0:
        temp_dice[0][1] = dice[0][1]
        temp_dice[2][1] = dice[2][1]
        temp_dice[1][0] = dice[3][1]
        temp_dice[1][1] = dice[1][0]
        temp_dice[1][2] = dice[1][1]
        temp_dice[3][1] = dice[1][2]
    elif dir == 1:
        temp_dice[0][1] = dice[3][1]
        temp_dice[2][1] = dice[1][1]
        temp_dice[1][0] = dice[1][0]
        temp_dice[1][1] = dice[0][1]
        temp_dice[1][2] = dice[1][2]
        temp_dice[3][1] = dice[2][1]
    elif dir == 2:
        temp_dice[0][1] = dice[0][1]
        temp_dice[2][1] = dice[2][1]
        temp_dice[1][0] = dice[1][1]
        temp_dice[1][1] = dice[1][2]
        temp_dice[1][2] = dice[3][1]
        temp_dice[3][1] = dice[1][0]
    else:
        temp_dice[0][1] = dice[1][1]
        temp_dice[2][1] = dice[3][1]
        temp_dice[1][0] = dice[1][0]
        temp_dice[1][1] = dice[2][1]
        temp_dice[1][2] = dice[1][2]
        temp_dice[3][1] = dice[0][1]

    dice_num = temp_dice[3][1]
    return temp_dice, dice_num

N, M, K = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

point = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for step in range(K):
    if step == 0:
        dir = 0
        x,y = 0, 0
        dice = [[0, 2, 0],
                [4, 1, 3],
                [0, 5, 0],
                [0, 6, 0]]
    #else:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        dir = (dir+2)%4
        nx = x + dx[dir]
        ny = y + dy[dir]
    dice, dice_num = move_dice(dice, dir)
    # 주사위칸 정수
    arr_num = arr[nx][ny]
    block_cnt = 1
    point_q = deque()
    visited = [[0]*M for _ in range(N)]
    visited[nx][ny] = 1
    point_q.append((nx, ny))
    while point_q:
        px, py = point_q.popleft()
        #visited[px][py] = 1
        for i in range(4):
            npx = px + dx[i]
            npy = py + dy[i]
           
            if 0 <= npx < N and 0 <= npy < M and arr[npx][npy] == arr_num and not visited[npx][npy]:
                #if step == K -1:
                #    print(npx, npy)
                block_cnt += 1
                visited[npx][npy] = 1
                point_q.append((npx, npy))
    point += block_cnt * arr_num

    x, y = nx, ny
    # 주사위 방향 이동
    if dice_num > arr_num:
        dir = (dir + 1)%4
    elif dice_num < arr_num:
        dir = (dir - 1)%4
    else:
        continue

# 예제 7, 8 틀림

print(point)