from collections import deque
import sys

def copy_fish():
    global arr
    result = dict()
    for i, j in arr:
        if len(arr[(i,j)]) >= 1:
            val = [item for item in arr[(i,j)]]
            result[(i,j)] = val
    return result

def rotate(x,y,d):
    global sx, sy, smell
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    origin_d = d
    for _ in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if not (nx == sx and ny == sy):
                if smell[(nx, ny)] < 0:
                    return nx, ny, d
        d = (d-1)%8
    return x, y, origin_d

def move_fish():
    global arr
    temp_arr = {(i,j): [] for i in range(4) for j in range(4)}
    for i, j in arr:
        for fish_dir in arr[(i,j)]:
            ni, nj, nd = rotate(i,j,fish_dir)
            if (ni, nj) not in temp_arr:
                temp_arr[(ni,nj)] = nd
            else:
                temp_arr[(ni,nj)].append(nd)
    arr = dict()
    for i, j in temp_arr:
        val = temp_arr[(i,j)]
        arr[(i,j)] = val
    return 

def shark_dfs(x, y, depth, fish_cnt, path):
    global arr, candidates
    temp_arr = dict()
    for i, j in arr:
        temp_arr[(i,j)] = [item for item in arr[(i,j)]]
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, -1, 0, 1]
    if depth == 3:
        candidates.append((fish_cnt, int(path)))
        return
    # dfs
    for i in range(1,5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            
            shark_dfs(nx, ny, depth+1, fish_cnt+len(temp_arr[(nx,ny)]), path+str(i))
            temp_arr[(nx, ny)] = []
    return 

def move_shark(day):
    global arr, sx, sy, candidates
    candidates = []
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, -1, 0, 1]

    shark_dfs(sx, sy, 0, 0, '')
    candidates.sort(key=lambda x: (-x[0], x[1]))
    path = str(candidates[0][1])
    print(candidates)
    # eat fish
    nx, ny = sx, sy
    for d in path:
        nx += dx[int(d)]
        ny += dy[int(d)]
        arr[(nx, ny)] = [] # remove fish
        smell[(nx, ny)] = day # left smell
    sx, sy = nx, ny
    return 

def remove_smell(day):
    global smell
    for i, j in smell:
        if smell[(i,j)] == day - 2 and smell[(i,j)] >= 0:
            smell[(i,j)] = -1000
    return

def finish(copied_fish):
    global arr
    for i, j in copied_fish:
        for f in copied_fish[(i,j)]:
            arr[(i,j)].append(f)
    return


def debug(arr):
    print("########")
    print(arr)

def main():
    global sx, sy, arr,  smell
    sys.stdin = open('/Users/sooyeon/programming/algorithm-study/baekJoon/test_23290.txt', 'r')
    M, S = map(int, input().split())
    arr = {(i,j): [] for i in range(4) for j in range(4)}
    smell = {(i,j): -1000 for i in range(4) for j in range(4)}
    for _ in range(M):
        r, c, d = map(int, input().split())
        if (r-1,c-1) not in arr:
            arr[(r-1,c-1)] = d-1
        else:
            arr[(r-1,c-1)].append(d-1)
           
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    for day in range(S):
        
        copied_fish = copy_fish()
        #debug(arr)
        move_fish()
        print('move fish', sx, sy)
        debug(arr)
        move_shark(day)
        # debug(arr)
        remove_smell(day)
        # debug(arr)
        finish(copied_fish)
        # debug(arr)
    result = 0
    for i, j in arr:
        result += len(arr[(i,j)])
    print(result)
    return

main()