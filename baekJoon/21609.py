import sys
from collections import deque

def debug(ls):
    print("##############")
    for l in ls:
        print(l)

def bfs(r,c,color):
    block, rainbow = [(r,c)], [] 
    q = deque()
    q.append((r,c))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    rainbow.append((nx, ny))
                    visited[nx][ny] = 2
                    q.append((nx, ny))
                elif arr[nx][ny] == color:
                    block.append((nx, ny))
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    if rainbow:
        for x, y in rainbow:
            visited[x][y] = 0 # 무지개는 어디든 포함될 수 있으므로
    if block:
        block.sort()
        std_x, std_y = block[0]
        path = block + rainbow
        #print(path)
        block_cnt = len(path)
        rainbow_cnt = len(rainbow)
        return block_cnt, rainbow_cnt, std_x, std_y, path
    return 0, 0, 0, 0, []

def gravity(arr):
    for r in range(N-2, -1, -1):
        for c in range(N):
            if arr[r][c] >= 0:
                q = deque()
                value = arr[r][c]
                
                q.append((r,c))
                while q:
                    x, y = q.popleft()
                    nx = x + 1
                    if 0 <= nx < N:
                        if arr[nx][y] < -1:
                            arr[nx][y] = value
                            arr[x][y] = -10
                            q.append((nx, y))
    return arr

N, color = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


point = 0
#max_path = []
#max_block, max_rainbow, max_x, max_y = 0, 0, 0, 0
# blocks list, rainbow list 따로 관리
while True:
    visited = [[0]*N for _ in range(N)]
    compare = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]: # 일반 블럭이고 방문하지 않았을 때
                visited[i][j] = 1
                blocks, rainbows, s_x, s_y, path = bfs(i, j, arr[i][j])
                compare.append((blocks, rainbows, s_x, s_y, path))
    if compare:
        # path 정렬
        compare.sort(reverse=True)
        
        if compare[0][0] <= 1: # 블럭의 개수는 2 이상
            break
        remove_block = compare[0][-1]
        point += len(remove_block)**2
        # 블럭 제거 
        for x, y in remove_block:
            arr[x][y] = -10
        
        # 중력 작용
        g_arr = gravity(arr)
        #debug(g_arr)
        # 회전
        rotate = [[arr[i][j] for i in range(N)] for j in range(N-1, -1, -1)]
        #debug(rotate)
        # 중력 작용
        arr = gravity(rotate)

        #debug(arr)
    else:
        break
print(point)
    
                



"""
point = 0
#while True:
group = []
#visited_block = [[0]*N for _ in range(N)]
max_block_cnt = 0
for p in range(N):
    for k in range(N):
        if arr[p][k] > 0:
            c = arr[p][k]
            q = deque()
            q.append((p, k, 1, 0, p, k, [(p,k)]))
            while q:
                x, y, block, rainbow, std_x, std_y, path = q.popleft()
                #print
                #print(block, x,y, std_x, std_y, path)
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in path:
                        if arr[nx][ny] == 0 or arr[nx][ny] == c:
                            #temp_rainbow = rainbow
                            #temp_std_x = std_x
                            #temp_std_y = std_y
                            # path는 값을 참조해야한다. 이동이 아니라 칸이 연결되어 있으면 되므로
                            #temp_path = path[:]
                            #temp_path.append((nx, ny))
                            path.append((nx, ny))
                            block += 1
                            if arr[nx][ny] == 0:
                                rainbow += 1
                                
                            elif arr[nx][ny] == c:
                                std_x = min(nx, std_x)
                                std_y = min(ny, std_y)
                            q.append((nx, ny, block, rainbow, std_x, std_y, path))       
                group.append((len(path), rainbow, std_x, std_y, path))    
            

#if len(group) <= 1:
    #break
group.sort(reverse=True)
remove_block = group[0][-1]
debug(group)
# remove block
for x, y in remove_block:
    arr[x][y] = -10
point += len(remove_block)**2
debug(arr)
# 중력 작용
g_arr = gravity(arr)

# 회전
rotate = [[arr[i][j] for i in range(N)] for j in range(N-1, -1,-1)]

# 중력 작용
arr = gravity(rotate)

debug(arr)
print(point)
"""

"""
point = 0
while True:
    group = []
    for i in range(N):
        for j in range(N):
            temp_color = []
            if arr[i][j] >= 0:
                
                for c in range(1, color+1):
                    if arr[i][j] == 0 or arr[i][j] == c:
                        q = deque()
                        q.append((i, j, 0, 0, 1e9, 1e9, []))
                        max_cnt = 0
                        max_temp = []
                        while q:
                            x, y, block, rainbow, std_x, std_y, path = q.popleft()
                            for i in range(4):
                                nx = x + dx[i]
                                ny = y + dy[i]
                                if nx < 0 or nx >= N or ny <0 or ny >= N:
                                    continue
                                if arr[nx][ny] < 0 or arr[nx][ny] != c:
                                    continue
                                temp_rainbow = rainbow
                                # 무지개
                                if arr[nx][ny] == 0:
                                    temp_rainbow += 1
                                # 일반
                                elif arr[nx][ny] == c:
                                    std_x = min(nx, std_x)
                                    std_y = min(ny, std_y)
                                temp_path = path[:]
                                temp_path.append((nx, ny))
                                # std_x, std_y 값 주의
                                q.append((nx, ny, block + 1, temp_rainbow,std_x, std_y, temp_path))
                                if block >= max_cnt:
                                    max_cnt = block
                                    max_temp.append((rainbow, std_x, std_y, temp_path))
                        if len(max_temp) > 0 and max_cnt >= 2:
                            max_temp.sort(reverse=True)
                            temp_color.append(max_temp[0])
            if len(temp_color) > 0:
                temp_color.sort(reverse=True)
                group.append(temp_color[0])
    if len(group) == 0:
        break
    group.sort(reverse=True)
    remove_block = group[0][-1]

    # remove block
    for x, y in remove_block:
        arr[x][y] = -10
    point += len(remove_block)**2

    # 중력 작용
    g_arr = gravity(arr)

    # 회전
    rotate = [[arr[i][j] for i in range(N)] for j in range(N-1, -1,-1)]

    # 중력 작용
    arr = gravity(rotate)

debug(arr)
"""