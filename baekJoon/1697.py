from collections import deque

def bfs(x, visited, time):
    q = deque()
    q.append((x, time))
    visited[x] = 1
    while q:
        nx, ntime = q.popleft()
        if nx == goal:
            print(ntime)
            return
        if nx >= 1 and not visited[nx-1]:
                q.append((nx-1, ntime+1))
                visited[nx-1] = 1
        if nx < 100000 and not visited[nx+1]:
                q.append((nx+1, ntime+1))
                visited[nx+1] = 1
        if 2*nx < 100001 and not visited[2*nx]:
                q.append((2*nx, ntime+1))
                visited[2*nx] = 1

start, goal = map(int, input().split())
visited = [0]*100001
bfs(start, visited, 0)