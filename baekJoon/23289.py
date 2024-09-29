from  collections import  deque

r, c= 7,8
hx, hy = 2,1

visited = [[0]*c for _ in range(r)]

q = deque()
q.append((hx,hy,5))
visited[hx][hy] = 1

dx=[-1, 0, 1]
dy=[1, 1, 1]
wind = 5
while q:

    x, y,wind = q.popleft()

    if wind > 1:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                q.append((nx, ny, wind-1))
                visited[nx][ny] = 1

print(visited)
