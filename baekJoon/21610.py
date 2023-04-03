import sys
from collections import deque

def debug(ls):
    for l in ls:
        print(l)
    print("-----------------")

def solution(d, dir):
    global cloud_q, water
    magic_list = []
    moved_cloud = deque()
    # move
    #print(cloud_q)
    while cloud_q:
        r, c = cloud_q.popleft()
        nr = r + dx[dir] * d
        nc = c + dy[dir] * d
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            value_r = abs(nr) // N + 1
            value_c = abs(nc) // N + 1
            nr = (nr + N * value_r) % N
            nc = (nc + N * value_c) % N
        moved_cloud.append((nr, nc))
    #print(moved_cloud)        
    # increase water
    while moved_cloud:
        r, c = moved_cloud.popleft()
        # rain
        water[r][c] += 1
        magic_list.append((r, c))
    
    # copy water
    for r, c in magic_list:
        for i in (1, 3, 5, 7):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and water[nr][nc] > 0:
                water[r][c] += 1
    
    # make cloud
    for i in range(N):
        for j in range(N):
            if water[i][j] >= 2:
                if (i, j) not in magic_list:
                    water[i][j] -= 2
                    cloud_q.append((i, j))
    #debug(water)

N, M = map(int, input().split())
water = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud_q = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
#cloud_q.append((N-1, ))
total_water = 0

for _ in range(M):
    dir, dist = map(int, sys.stdin.readline().split())
    solution(dist, dir-1)

for i in range(N):
    for j in range(N):
        total_water += water[i][j]

print(total_water)