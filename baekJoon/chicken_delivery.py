from collections import deque

n, m = map(int, input().split())
chicken2, house = [], []
array = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken2.append((r,c))
    array.append((data))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#집의 x, y를 입력 받아서 dist 찾기
def bfs(now_x, now_y):
    q = deque([(now_x, now_y)])
    dist = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #치킨집을 찾아서 결과값 return
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if array[nx][ny] == 2 and not visited[nx][ny]:
                dist += 1
                visited[nx][ny] = 1
                break
            elif array[nx][ny] == 0 and not visited[nx][ny]:
                dist += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    print(dist)
    return dist

def combinations(data, length):
    r = []
    def dfs(cur, pos):
        if len(cur) == length:
            r.append(cur)
        if pos == len(data):
            return
        if type(data) is list:
            for i in range(pos, len(data)):
                dfs(cur + [data[i]], i + 1)
        else:
            for i in range(pos, len(data)):
                dfs(cur + data[i], i + 1)
    if type(data) is list:
        dfs([], 0)
    else:
        dfs("", 0)
    return r


chicken = deque()
for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chicken.append((i, j))

for x, y in chicken:
    array[x][y] = 0
#조합 생성
comb_arr = list(range(1, m+1))
comb_list = []
for i in range(m, 0, -1):
    comb_list.append(combinations(comb_arr, i))

dist = 0
result = 1e9
comb_list2 = combinations(chicken2, m)
"""
#메인함수
for lst in comb_list2:
    now_dist = 0
    visited = [[0] * n for _ in range(n)]
    for i in lst:
        x = chicken[i-1][0]
        y = chicken[i-1][1]
        array[x][y] = 2

    for i in range(n):
        for j in range(n):
            if array[i][j] == 1 and not visited[i][j]:
                visited[i][j]=1
                now_dist += bfs(i, j)

    for i in lst:
        x = chicken[i-1][0]
        y = chicken[i-1][1]
        array[x][y] = 0
    print(now_dist)
    if now_dist < result:
        result = now_dist
"""

for lst in comb_list2:
    now_dist=0
    visited= [[0]*n for _ in range(n)]
    for i in range(m):
        chx = lst[i][0]
        chy = lst[i][1]
        array[chx][chy] = 2
    for hox, hoy in house:
        if not visited[hox][hoy]:
            visited[hox][hoy]=1
            now_dist += bfs(hox, hoy)
    print(dist)
    print(array)
    for i in range(m):
        chx = lst[i][0]
        chy = lst[i][1]
        array[chx][chy] = 0
    if now_dist < result:
        result = now_dist


print(result)