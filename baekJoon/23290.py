import sys
from copy import deepcopy
from collections import deque

global sx, sy

def debug(ls):
    print("##################")
    for l in ls:
        print(l)

def dfs(x, y, path, visited):
    visited=[]
    if len(path) == 3:
        print(path)
        move_shark.append(path)
        return 
    flag = 1
    for tx, ty in path:
        if x == tx and y == ty:
            flag = 0
            break
    if flag:
        path.append((x, y))
        for i in range(4):
            nx = x + sx[i]
            ny = y + sy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                #path.append((nx, ny))
                dfs(nx, ny, path, visited)

M, S = map(int, input().split())
arr = {(i, j): deque() for i in range(4) for j in range(4)}

for _ in range(M):
    r, c, d = map(int, input().split())
    arr[(r-1,c-1)].append(d-1)

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1
smell = [[0]*4 for _ in range(4)]

fr = [0, -1, -1, -1, 0, 1, 1, 1]
fc = [-1, -1, 0, 1, 1, 1, 0, -1]

sx = [-1, 0, 1, 0]
sy = [0, -1, 0, 1]

for s in range(1,S+1):
    # 상어 복제
    temp_arr = deepcopy(arr)
    # 물고기 이동
    for r in range(4):
        for c in range(4):
            if temp_arr[(r,c)]:
                for i in range(len(arr[(r,c)])): # temp_arr에서 pop이 일어나므로 index가 범위 밖으로 안 나가게 하기 위해
                    fish_dir = arr[(r,c)][i]
                    origin_fish_dir = fish_dir
                    nr = r + fr[fish_dir]
                    nc = c + fc[fish_dir]
                    if 0<= nr <4 and 0<= nc < 4 and not (nr == shark_x and nc == shark_y) and not smell[nr][nc]:
                        
                        temp_arr[(r,c)].remove(fish_dir)
                        temp_arr[(nr,nc)].append(fish_dir)
                        
                    else: # 자신 방향대로 이동 실패할 경우
                        for _ in range(8):
                            fish_dir -= 1
                            fish_dir = fish_dir % 8
                            nr = r + fr[fish_dir]
                            nc = c + fc[fish_dir]
                            if 0<= nr <4 and 0<= nc < 4 and not (nr == shark_x and nc == shark_y) and not smell[nr][nc]:
                                #print(temp_arr[r][c], nr, nc, fish_dir)
                                temp_arr[(r,c)].remove(origin_fish_dir)
                                temp_arr[(nr,nc)].append(fish_dir)
                                break
    #debug(temp_arr)
    # 상어 이동 방법 탐색
    move_shark = []
    q = deque()
    q.append(((shark_x, shark_y), [(shark_x, shark_y)], 0, ''))
    while q:
        p, path, cnt, dir = q.popleft()
        x, y = p[0], p[1]
        if cnt == 3:
            sum_fish = 0
            path_q = deque(path)
            while path_q:
                x,y = path_q.popleft()
                if (x,y) not  in path_q: # 재방문을 해도 되므로 재방문하는 경우는 물고기수 더하지 않음
                    sum_fish += len(temp_arr[(x,y)])
                #print(sum_fish, temp_arr[x][y])
            move_shark.append((sum_fish, dir, path))
        if cnt < 3:
            for idx in range(4):
                nx = x + sx[idx]
                ny = y + sy[idx]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    #if (nx,ny) not in path:
                    temp_path = path[:] # path 배열이 공유되지 않도록 복제
                    temp_path.append((nx, ny))
                    q.append(((nx, ny), temp_path, cnt+1, dir+str(idx)))
    # 상어 이동 방법 선택 및 물고기 냄새 생성
    move_shark.sort(key=lambda x: (-x[0], x[1], x[2]))
    shark_path = move_shark[0][-1] # 이동방법 선택
    for i in range(1,4): # 첫번째 시작하는 상어 좌표값에서는 물고기를 없앨 필요 없음. 물고기와 상어 함께 존재 가능
        x, y = shark_path[i]
        if temp_arr[(x,y)]:
            temp_arr[(x,y)] = [] # 물고기 제거
            smell[x][y] = s # 몇번째에서 냄새가 남았는지 입력
    shark_x, shark_y = move_shark[0][-1][-1] # 마지막으로 이동한 좌표값이 현재 상어의 좌표 값

    # 두번 전에 생긴 냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[i][j] == s-2:
                smell[i][j] = 0

    # 복제된 상어 추가
    for i in range(4):
        for j in range(4):
            if arr[(i,j)]:
                for fish_dir in arr[(i,j)]:
                    temp_arr[(i,j)].append(fish_dir)

    arr = deepcopy(temp_arr)

    #debug(arr)
    #debug(smell)
left_fish = 0
for i in range(4):
    for j in range(4):
        left_fish += len(arr[(i,j)])

print(left_fish)


"""
for s in range(1,S+1):
    # 상어 복제
    temp_arr = deepcopy(arr)
    # 물고기 이동
    for r in range(4):
        for c in range(4):
            if temp_arr[r][c]:
                for i in range(len(arr[r][c])): # temp_arr에서 pop이 일어나므로 index가 범위 밖으로 안 나가게 하기 위해
                    fish_dir = arr[r][c][i]
                    origin_fish_dir = fish_dir
                    nr = r + fr[fish_dir]
                    nc = c + fc[fish_dir]
                    if 0<= nr <4 and 0<= nc < 4 and not (nr == shark_x and nc == shark_y) and not smell[nr][nc]:
                        
                        temp_arr[r][c].remove(fish_dir)
                        temp_arr[nr][nc].append(fish_dir)
                        
                    else: # 자신 방향대로 이동 실패할 경우
                        for _ in range(8):
                            fish_dir -= 1
                            fish_dir = fish_dir % 8
                            nr = r + fr[fish_dir]
                            nc = c + fc[fish_dir]
                            if 0<= nr <4 and 0<= nc < 4 and not (nr == shark_x and nc == shark_y) and not smell[nr][nc]:
                                #print(temp_arr[r][c], nr, nc, fish_dir)
                                temp_arr[r][c].remove(origin_fish_dir)
                                temp_arr[nr][nc].append(fish_dir)
                                break
    #debug(temp_arr)
    # 상어 이동 방법 탐색
    move_shark = []
    q = deque()
    q.append(((shark_x, shark_y), [(shark_x, shark_y)], 0, ''))
    while q:
        p, path, cnt, dir = q.popleft()
        x, y = p[0], p[1]
        if cnt == 3:
            sum_fish = 0
            path_q = deque(path)
            while path_q:
                x,y = path_q.popleft()
                if (x,y) not  in path_q: # 재방문을 해도 되므로 재방문하는 경우는 물고기수 더하지 않음
                    sum_fish += len(temp_arr[x][y])
                #print(sum_fish, temp_arr[x][y])
            move_shark.append((sum_fish, dir, path))
        if cnt < 3:
            for idx in range(4):
                nx = x + sx[idx]
                ny = y + sy[idx]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    #if (nx,ny) not in path:
                    temp_path = path[:] # path 배열이 공유되지 않도록 복제
                    temp_path.append((nx, ny))
                    q.append(((nx, ny), temp_path, cnt+1, dir+str(idx)))
    # 상어 이동 방법 선택 및 물고기 냄새 생성
    move_shark.sort(key=lambda x: (-x[0], x[1], x[2]))
    shark_path = move_shark[0][-1] # 이동방법 선택
    for i in range(1,4): # 첫번째 시작하는 상어 좌표값에서는 물고기를 없앨 필요 없음. 물고기와 상어 함께 존재 가능
        x, y = shark_path[i]
        if temp_arr[x][y]:
            temp_arr[x][y] = [] # 물고기 제거
            smell[x][y] = s # 몇번째에서 냄새가 남았는지 입력
    shark_x, shark_y = move_shark[0][-1][-1] # 마지막으로 이동한 좌표값이 현재 상어의 좌표 값

    # 두번 전에 생긴 냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[i][j] == s-2:
                smell[i][j] = 0

    # 복제된 상어 추가
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                for fish_dir in arr[i][j]:
                    temp_arr[i][j].append(fish_dir)

    arr = deepcopy(temp_arr)

    #debug(arr)
    #debug(smell)
left_fish = 0
for i in range(4):
    for j in range(4):
        left_fish += len(arr[i][j])

print(left_fish)
"""
