from _collections import deque

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
visited = [[0]*n for _ in range(n)]
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

#기준색상 별 시작점 찾기
def start(standard):
    for i in range(n):
        for j in range(n):
            if array[i][j] == standard:
                return i, j
#기준별 블럭
def find(now_x, now_y, standard):
    q = deque([(now_x, now_y)])
    visited[now_x][now_y] = 1
    xynum = deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            color = array[nx][ny]
            if color == 0 and visited[nx][ny]==0:
                q.append((nx, ny))
                xynum.append((nx, ny))
            if color == standard and visited[nx][ny] == 0:
                q.append((nx, ny))
                xynum.append((nx, ny))
                visited[nx][ny] = 1
    if len(xynum)==1:
        xynum = None
    return xynum
# 값 지우기
def remove(xynum):
    while xynum:
        findx, findy = xynum.popleft()
        for i in range(n):
            for j in range(n):
                if findx==i and findy==j:
                    array[i][j] = -2
#점수계산
def points(xynum):
    p = len(xynum)
    return p**2
#다음 블럭 확인
def check_block(now_x, now_y):
    for x in range(now_x, n-1):
        if array[x+1][now_y] > -2:
            return x
#중력 작용
def gravity(array):
    for i in range(n):
        for j in range(n):
            color = array[i][j]
            if color > -2:
                x = check_block(i, j)
                if x is None:
                    continue
                array[x][j] = color
#회전
def turn(now_x, now_y):
    y = now_x
    x = 0
    if now_y == 0:
        x = 4
    elif now_y == 1:
        x = 3
    elif now_y == 2:
        x = 2
    elif now_y == 3:
        x = 1
    elif now_y == 4:
        x = 0
    return x, y
#블럭 비교
def get_max(standard, comparison, xyqueue):
    max_index = 0
    max_num = -1
    max_rainbow = -1
    for i in range(standard):
        if comparison[i]:
            rainbow_cnt = 0
            nblock = len(comparison[i])
            rainx, rainy = comparison[i].popleft()
            while comparison[i]:
                if array[rainx][rainy] == 0:
                    rainbow_cnt += 1
            if nblock > max_num:
                max_num = nblock
                max_index = i
            elif nblock == max_num:
                if rainbow_cnt > max_rainbow:
                    max_num=nblock
                    max_index = i
                elif rainbow_cnt == max_rainbow:
                    now_x, now_y = xyqueue[i]
                    mx, my = xyqueue[max_index]
                    if now_x > mx:
                        max_num = nblock
                        max_index = i
                    elif now_y > my:
                        max_num = nblock
                        max_index = i
    return max_index

point = 0
while True:
    comparison = deque()
    xyqueue = deque()
    for standard in range(1, m+1):
        now_x, now_y = start(standard)
        xyqueue.append((now_x, now_y))
        xynum = find(now_x, now_y, standard)
        comparison.append(xynum)
    if len(comparison)==0:
        print(point)
        break
    print(comparison)
    print(get_max(m, comparison, xyqueue))
    final_xynum = comparison[get_max(m, comparison, xyqueue)]
    print(final_xynum)
    remove(final_xynum)
    point += points(final_xynum)
    gravity(array)
    turned_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turned_x, turned_y = turn(i, j)
            turned_array[turned_x][turned_y] = array[i][j]
    array = turned_array
    gravity(array)