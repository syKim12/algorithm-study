
import sys
from collections import deque

global N

def debug(d):
    print("################")
    for i in d.items():
        print(i)
    return


def move(speed, dir, x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1] 
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    # 새 좌표값 생성
    nx = x + speed * dx[dir]
    ny = y + speed * dy[dir]
    # 행과 열의 양 끝이 연결
    nx = nx % N
    ny = ny % N
    return nx, ny


N, M, K = map(int, sys.stdin.readline().split())

shark_d = {(i, j): deque() for i in range(N) for j in range(N)}

for _ in range(M):
    r, c, mass, speed, dir = map(int, sys.stdin.readline().split())
    shark_d[(r-1,c-1)].append((mass, speed, dir))



for _ in range(K):
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                while shark_d[(i, j)]:
                    m, s, d = shark_d[(i, j)].popleft()
                    ni, nj = move(s, d, i, j)
                    visited[ni][nj] = 1
                    print(i, j, ni, nj)
                    shark_d[(ni, nj)].append((m, s, d))
    print("!!!!!!!")
    debug(shark_d)
    for i in range(N):
        for j in range(N):
            if len(shark_d[(i, j)])>1:
                temp_dir = set()
                dir_flag = 0 # 모두 짝수이거나 홀수
                sum_mass, sum_speed, cnt = 0, 0, 0
                while shark_d[(i, j)]:
                    m, s, d = shark_d[(i, j)].popleft()
                    sum_mass += m
                    sum_speed += s
                    cnt += 1
                    temp_dir.add(d%2)
                for i in range(1,len(temp_dir)):
                    if temp_dir[i] != temp_dir[i-1]:
                        dir_flag = 1
                        break
                nm = sum_mass // 5
                if nm > 0:
                    ns = sum_speed // cnt
                    for p in range(dir_flag, 8, 2):
                        ni, nj = move(ns, p, i, j)
                        shark_d[(ni, nj)].append((nm, ns, p))


                debug(shark_d)
debug(shark_d)