import sys
from collections import deque

global N

def debug(d):
    print("################")
    for i in d.items():
        print(i)
    return


def move(speed, d, x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1] 
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    # 새 좌표값 생성
    nx = x + speed * dx[d]
    ny = y + speed * dy[d]
    # 행과 열의 양 끝이 연결
    nx = nx % N
    ny = ny % N
    return nx, ny

def move_fireballs():
    global shark_d
    move_shark = dict()
    for k, v in shark_d.items():
        temp_v = [l for l in v]
        move_shark[k] = temp_v
    for i, j in shark_d:
        #print(i,j)
        for m, s, d in shark_d[(i,j)]:
            ni, nj = move(s,d,i,j)
            if len(shark_d[(ni, nj)]) >= 0: 
                move_shark[(ni, nj)].append((m, s, d))
                move_shark[(i,j)].pop(0)
                #print('move: ',i,j, ni, nj, move_shark[(ni,nj)])
    shark_d = dict()
    for k, v in move_shark.items():
        temp_v = [l for l in v]
        shark_d[k] = temp_v
    return

def magic():
    global shark_d
    move_shark = dict()
    for k, v in shark_d.items():
        temp_v = [l for l in v]
        move_shark[k] = temp_v

    for i, j in move_shark:
        if len(move_shark[(i,j)]) > 1:
            temp_sum = 0
            temp_s = 0
            temp_before = move_shark[(i,j)][0][-1]%2
            #print(move_shark[(i,j)])
            for m,s,d in move_shark[(i,j)]:
                temp_sum += m
                temp_s += s
            for m,s,d in move_shark[(i,j)]:
                if d % 2 != temp_before:
                    temp_flag = 1
                    break
                temp_flag = 0
            #print(temp_flag)
            temp_mass = temp_sum // 5
            temp_speed = temp_s//len(move_shark[(i,j)])
            move_shark[(i,j)] = []
            for d in range(temp_flag, 8, 2):
                if temp_mass > 0:
                    move_shark[(i,j)].append((temp_mass, temp_speed, d))
                    #print(nx,ny)
            
        

    shark_d = dict()
    for k, v in move_shark.items():
        temp_v = [l for l in v]
        shark_d[k] = temp_v
    return

N, M, K = map(int, sys.stdin.readline().split())

shark_d = {(i, j): [] for i in range(N) for j in range(N)}

for _ in range(M):
    r, c, mass, speed, d = map(int, sys.stdin.readline().split())
    shark_d[(r-1,c-1)].append((mass, speed, d))

cnt = 0
for _ in range(K):
    move_fireballs()
    magic()

result = 0
for i, j in shark_d:
    for m, s, d in shark_d[(i,j)]:
        result += m

print(result)
