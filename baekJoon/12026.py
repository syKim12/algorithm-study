import sys

def dfs(path, energy, flag, cnt): #cnt는 움직인 횟수
    if len(path) == N and path[-1] == flag:
        min_energy = min(min_energy, energy)
        return
    for i in range(N):
        if not visited[i]:
            if dist[i] == 'B':
                flag = 'O'
                
            elif dist[i] == 'O':
                flag = 'J'
            else:
                flag = "B"
            visited[i] = 1
            path.append()
            dfs(path, ,flag)
            visited[i] = 0
            path.pop()

N = int(input())
dist = [i for i in sys.stdin.readline().strip()]
min_energy = 1e9
visited = [0]*N

dfs([], 0)
print(min_energy)