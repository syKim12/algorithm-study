from collections import deque
import sys

def debug(ls):
    print("#######")
    for l in ls:
        print(l)


def bfs(x,y, num):
    global arr, N, visited
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    
    visited[x][y] = 1
    cnt = 1
    std_x = x
    std_y = y
    path = [(x,y)]
    q.append((x,y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i] 
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == num or arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if arr[nx][ny] != 0:
                        std_x = min(std_x, nx)
                        std_y = min(std_y, ny)
                    cnt += 1
                    q.append((nx, ny))
                    path.append((nx,ny))
    return cnt, std_x, std_y, path

def find_group():
    global arr, N, visited, remove_list
    candidates = []
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > 0:
                cnt, std_x, std_y, path = bfs(r,c, arr[r][c])
                if cnt >= 2:
                    candidates.append((cnt, std_x, std_y, path))
    candidates.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    # print(candidates)
    if len(candidates) == 0:
        return 0
    remove_list = candidates[0][3]
    return 1

def remove():
    global arr, remove_list, point
    for x, y in remove_list:
        arr[x][y] = -10
    point += len(remove_list)**2
    return

def gravity():
    global N, arr
    for c in range(N):
        for r in range(N-2, -1, -1):
            if arr[r][c] >= 0:
                
                if arr[r+1][c] == -10:
                    arr[r+1][c] = arr[r][c]
                    arr[r][c] = -10
                
    # debug(arr)
    return

def rotate():
    global N, arr
    rotated = []
    for c in range(N-1, -1, -1):
        temp = [arr[r][c] for r in range(N)]
        rotated.append(temp)
    # debug(rotated)
    return rotated


def main():
    global arr, N, point
    sys.stdin = open('21609_test.txt', 'r')
    N, M = map(int, input().split())
    arr = []
    point = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    while find_group():
        remove()
        gravity()
        arr = rotate()
        print('rotate')
        debug(arr)
        gravity()
        debug(arr)

        print(point)


main()