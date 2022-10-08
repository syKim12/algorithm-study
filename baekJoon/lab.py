# make a combination, then calculate
from itertools import combinations
from collections import deque
"""
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
"""

n, m = map(int, input().split())
wall, virus, blank = [], [], []
array = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
        

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(m):
        if data[c] == 1:
            array[r][c] = 1
            wall.append((r, c))
        elif data[c] == 2:
            array[r][c] = 2
            virus.append((r, c))
        else:
            blank.append((r, c))

candidates = combinations(blank, 3)

for candidate in candidates:
    q = deque(candidate)
    while q:
        x, y = q.popleft()
        array[x][y] = 1
    bfs()    
    