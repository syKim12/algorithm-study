import sys
from collections import deque

def debug(ls):
    print("###########")
    for l in ls:
        print(l)

def magic(dist, d):
    global arr, N
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    nx, ny = N//2, N//2
    for _ in range(dist):
        nx += dx[d]
        ny += dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        arr[nx][ny] = 0
    return

def get_next_dfs(idx):
    global path,arr
    if idx == len(path) - 1:
        return -1
    else:
        if arr[path[idx][0]][path[idx][1]] > 0:
            return idx
        get_next(idx)

def get_next(idx):
    global path, arr
    q = deque()
    q.append(idx)
    while q:
        i = q.popleft()
        if arr[path[i][0]][path[i][1]] > 0:
            return i
    return

def move():
    global path, arr
    for i in range(len(path)):
      r, c = path[i]
      if arr[r][c] == 0:
        flag = 0
        #if i + 1 < len(path):
            # nr, nc = path[get_next(i+1)]
            # arr[r][c] = arr[nr][nc]
            # arr[nr][nc] = 0
        for j in range(i+1,len(path)):
            nr, nc = path[j]
            if arr[nr][nc] > 0:
                flag = 1
                arr[r][c] = arr[nr][nc]
                arr[nr][nc] = 0
                break
        if not flag:  # 0보다 큰 값 없으면 탐색 끝!!!
            return
    return

def make_path(n):
    path = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    x, y = n//2, n//2
    d = 0
    flag = 0
    for i in range(1,n+1):
        for _ in range(2):
            for j in range(i):
                x += dx[d]
                y += dy[d]
                if x < 0 or y < 0:
                    flag = 1
                    break
                path.append((x,y))
            d = (d+1)%4
            if flag:
                break
        if flag:
            break
    # print(path)
    return path

def explode():
    global arr, path
    cnt = 0
    num = 0
    temp = []
    explosion = 0
    l = []
    for i in range(len(path)):
      r, c = path[i]
      if arr[r][c] != num:
        if cnt >= 4:
          #for x, y in temp:
          #  explosion += arr[x][y]
          #  arr[x][y] = 0
          l += temp
        num = arr[r][c]
        cnt = 1
        temp = [(r, c)]
      else:
        temp.append((r, c))
        cnt += 1
    for x, y in l:
        explosion += arr[x][y]
        arr[x][y] = 0
    return explosion

def copy(arr):
    global N, path
    copied_arr = [[0]*N for _ in range(N)]
    # 개수, 구슬 번호 저장
    num = 0
    cnt = 0
    last_idx = -1
    fill = []
    for i in range(len(path)):
      r, c = path[i]
      if num != arr[r][c]:
        if cnt > 0:
          if last_idx + 2 < len(path):
            copied_arr[path[last_idx+1][0]][path[last_idx+1][1]] = cnt
            copied_arr[path[last_idx+2][0]][path[last_idx+2][1]] = num
            last_idx += 2
          else:
            if last_idx + 1 == len(path) - 1:
              copied_arr[path[last_idx+1][0]][path[last_idx+1][1]] = cnt
            break
        num = arr[r][c]
        cnt = 1
      else:
        cnt += 1
    return copied_arr

def main():
    global arr, path, N
    sys.stdin = open('21611_test.txt', 'r')
    N, M = map(int, input().split())
    arr = []
    result = 0

    for _ in range(N):
        temp_input = list(map(int, input().split()))
        arr.append(temp_input)
    path = make_path(N)
    for _ in range(M):
        d, dist = map(int, input().split())
        magic(dist, d-1)
        move()
        # debug(arr)
        while True:
            explosion = explode()
            if explosion > 0:
                result += explosion
                move()
                # print('explode')
                # debug(arr)
                
            else:
                break
        arr = copy(arr)
        # print('copy')
        debug(arr)
 
    print(result)
    return

main()
