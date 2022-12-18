from collections import deque
n, m = map(int, input().split())
now_x, now_y, now_face = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change(i):
    if i == 0:
        return 3
    elif i == 1:
        return 0
    elif i == 2:
        return 1
    elif i == 3:
        return 2

def back(i):
    if i == 0:
        return 2
    elif i == 1:
        return 3
    elif i == 2:
        return 0
    elif i == 3:
        return 1


def bfs(now_x, now_y, now_face):
    result = 1
    q = deque([(now_x, now_y, now_face)])
    array[now_x][now_y] = 2
    while q:
        x, y, face = q.popleft()
        temp_face = face
        for i in range(4):
            temp_face = change(temp_face)
            nx = x + dx[temp_face]
            ny = y + dy[temp_face]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and array[nx][ny] == 0:
                result += 1
                array[nx][ny] = 2
                q.append((nx, ny, temp_face))
                break

            elif i == 3:
                nface = back(face)
                nx = x + dx[nface]
                ny = y + dy[nface]
                if array[nx][ny] == 1:
                    return result
                else:
                    array[nx][ny] = 2
                    q.append((nx, ny, face))

print(bfs(now_x, now_y, now_face))