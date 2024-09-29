import sys
from collections import deque
from copy import deepcopy

def debug(li):
    print("###############")
    for l in li:
        print(l)


N, Q = map(int, input().split())
arr = []
for _ in range(2**N):
    arr.append(list(map(int, sys.stdin.readline().split())))

step = list(map(int, sys.stdin.readline().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(len(step)):
    # 회전
    L = step[i]
    shark = [[(r, c) for r in range(2**L-1, -1, -1)] for c in range(2**L)] # 어떤 좌표값을 참조해야하는지 알려주는 배열
    times = 2 ** (N-L)
    temp_arr = [[(0,0) for _ in range(2**N)] for j in range(2**N)]
    for start_x in range(0, 2**N, 2**L):
        for start_y in range(0, 2**N, 2**L):
            for i in range(2**L):
                for j in range(2**L):
                    nx = start_x + i
                    ny = start_y + j
                    which_x, which_y = shark[i][j] # 어떤 값을 참조해야할지 알려줌
                    temp_arr[nx][ny] = arr[start_x + which_x][start_y + which_y]
    arr = temp_arr
    origin_arr = deepcopy(arr) # 얼음 값을 제거하면서 값을 잘못 참조할 수 있으므로 기존 값 보존
    # 얼음 감소
    for x in range(2**N):
        for y in range(2**N):
            ice_cnt = 0
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and origin_arr[nx][ny] > 0:
                    ice_cnt += 1
            if ice_cnt < 3 and origin_arr[x][y] > 0:   
                arr[x][y] -= 1 # 인접한 얼음 개수 2 이하일 경우 얼음 수 감소
    
left_ice = 0
for x in range(2**N):
    for y in range(2**N):
        left_ice += arr[x][y]

max_block_cnt = 0
visited = [[0]*(2**N) for _ in range(2**N)]
for r in range(2**N):
    for c in range(2**N):
        if arr[r][c] and not visited[r][c]> 0:
            q = deque()
            q.append((r, c))  
            block_cnt = 0
            while q:
                r_p, c_p = q.popleft()
                for i in range(4):
                    nr = r_p + dx[i]
                    nc = c_p + dy[i]
                    if 0 <= nr < 2**N and 0 <= nc < 2**N and not visited[nr][nc]:
                        if arr[nr][nc] > 0:

                            visited[nr][nc] = 1
                            #print(nr, nc, block_cnt)
                            q.append((nr, nc))
                            block_cnt += 1
            max_block_cnt = max(max_block_cnt, block_cnt)

#debug(arr)                      
print(left_ice)
print(max_block_cnt)
