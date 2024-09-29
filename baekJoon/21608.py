import sys
from collections import deque

global arr, order_l, like_d, dx, dy

def debug(l):
    print("************")
    for item in l:
        print(item)
"""
def find_student(num):
    max_like = 0
    compare_l = []
    start_x, start_y = 0, 0
    q = deque()
    q.append((start_x, start_y))
    visited = [[0] * N for _ in range(N)]
    while q:
        cnt = 0 # 칸 하나하나의 인접칸 학생 체크해야하므로 카운트 값 초기화
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]: # queue에 인접한 현재칸에서 이동가능한 칸 추가
                    q.append((nx, ny))
                if arr[x][y] == 0 and arr[nx][ny] in like_d[num]: # 현재칸에서 인접한 좋아하는 학생수 카운트
                    cnt += 1       
        if max_like == cnt:
            compare_l.append((x,y))
        elif max_like < cnt:
            max_like = cnt
            compare_l = [(x,y)] # 더 크므로 후보군 리스트 리셋
    return max_like, compare_l

def find_empty(compare_l):
    max_empty = 0
    compare_row_col = []
    for x, y in compare_l:
        if arr[x][y] == 0:
            empty_cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                    empty_cnt += 1
            if empty_cnt == max_empty:
                compare_row_col.append((x,y))
            elif empty_cnt > max_empty:
                max_empty = empty_cnt
                compare_row_col = [(x,y)]

    if len(compare_row_col) > 1: # 중복될 경우 행열 번호가 가장 작은 것이 우선
        compare_row_col.sort() 
        #print(compare_row_col)
    fill_x, fill_y = compare_row_col[0]    

    return fill_x, fill_y
"""

"""
def find(num):
    q = deque()
    q.append((0, 0))
    visited = [[0]*N for _ in range(N)]
    temp = []
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        like_cnt, empty_cnt = 0, 0
        for i  in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 다음 칸으로 이동
                if not visited[nx][ny]:
                    q.append((nx, ny))
                if arr[x][y] == 0: # 중심칸에 숫자를 채울 수 있다면 추가
                    # 비어있는 칸
                    if arr[nx][ny] == 0:
                        empty_cnt += 1
                    # 좋아하는 학생 수
                    elif arr[nx][ny] in like_d[num]:
                        like_cnt += 1
        if arr[x][y] == 0:
            temp.append((like_cnt, empty_cnt, x, y))
    ######## key point
    temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3])) 
    ########
    final_x, final_y = temp[0][2], temp[0][3]
    return final_x, final_y         

"""

def find(num):
    temp = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                
                like_cnt, empty_cnt = 0,0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 0:
                            empty_cnt += 1
                        elif arr[nx][ny] in like_d[num]:
                            like_cnt += 1
                temp.append((like_cnt, empty_cnt, x, y))
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    final_x, final_y = temp[0][2], temp[0][3]
    return final_x, final_y

N = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
arr = [[0] * N for _ in range(N)]

order_l, like_d = [], {}

for _ in range(N**2):
    num, a, b, c, d = map(int, sys.stdin.readline().split())
    order_l.append(num)
    like_d[num] = [a, b, c, d]


# 순서대로 칸에 채워 넣는다
for i in range(N**2):
    fill_x, fill_y = find(order_l[i])
    arr[fill_x][fill_y] = order_l[i]

#debug(arr)

# 점수 계산
result = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] in like_d[arr[x][y]]:
                cnt += 1 
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000
print(result)

