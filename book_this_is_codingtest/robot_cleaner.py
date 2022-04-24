from collections import deque
n, m = map(int, input().split())
now_x, now_y, now_face = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*n for _ in range(n)]



def change(i):
    if i == 0:
        return 3
    elif i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return 2

def back(i):
    if i == 0:
        return 2
    elif i == 1:
        return 3
    elif i == 2:
        return 0
    else:
        return 1


def bfs(now_x, now_y, now_face):
    cnt = 0
    result = 1
    #visited[now_x][now_y] = 1
    q = deque([(now_x, now_y, now_face)])
    while q:
        x, y, face = q.popleft()
        for i in range(4):
            nface = change(i)
            nx = x + dx[nface]
            ny = y + dy[nface]
            if cnt >= 4:
                cnt = 0
                nface = back(i)
                nx = x + dx[nface]
                ny = y + dy[nface]
                if array[nx][ny] == 1 and visited[nx][ny] == 0:
                    return result
                    #break
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny, nface))
            else:
                visited[now_x][now_y] = 1
                #cnt += 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                cnt += 1
                if array[nx][ny] == 0 and visited[nx][ny] == 0:
                    result += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, nface))
                else:
                    q.append((x, y, nface))


print(bfs(now_x, now_y, now_face))