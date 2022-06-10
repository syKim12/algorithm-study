#시간 초과
"""
n, m = map(int, input().split())
table = []
for _ in range(n):
    k = input()
    table.append([k[i] for i in range(m)])
#dx = [-1, 0, 1, 0]
#dy = [0, -1, 0, 1]
result = []
#visited = [[0]*m for _ in range(n)]
total_num = n*m
def dfs(i, x, y, path, cnt):
    if x < 0 or x >= n or y < 0 or y >= m:
        result.append(cnt)
        return
    #if visited[x][y]:
    #    return
    s = table[x][y]
    for k in path:
        if k == s:
            return
    if i == total_num:
        result.append(cnt)
        return
    temp = path[0:]
    temp.append(s)
    cnt += 1
    dfs(i + 1, x + 1, y, temp, cnt)
    dfs(i + 1, x, y + 1, temp, cnt)
    dfs(i + 1, x - 1, y, temp, cnt)
    dfs(i + 1, x, y - 1, temp, cnt)
dfs(0, 0, 0, path=[], cnt = 0)
print(max(result))
"""
#list가 아닌 set을 이용하여 시간을 단축 시킨 코드
#from https://sorryhyeon.tistory.com/34
r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny]) #최대 칸수가 아닌 경우 돌아가기 위해 값을 제거해준다
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)