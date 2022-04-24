from collections import deque

INF = 1e9

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 거리 계산
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if dist == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


# 거리 지점 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and array[i][j] < now_size and 1 <= array[i][j]:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


ate = 0
result = 0

while True:
    value = find(bfs())
    if value is None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        ate += 1
        array[now_x][now_y] = 0
        if ate >= now_size:
            now_size += 1
>>>>>>> 9f47cc1a52868e9534f08e2ab1bbec83c79eb666
            ate = 0