import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0]*N 
visited = [[0]*M for _ in range(N)]
candidates = []
for i in range(N):
    arr[i] = sys.stdin.readline().strip()
min_cnt = 1e9
"""
def sol(path, visited, idx):
    if idx == N:
        cnt = 0
        one_array = ''

    for i in range(0, N-6): # 세로 i
        for j in range(7, M-6): # 가로 j
            if not visited[i][j]:
                visited[i][j] = 1
                path.append((i, j))
                sol(path, visited, idx + 1)
                visited[i][j] = 0
                path.pop()
"""
for i in range(7, N-6):
    for j in range(0, M-6):
        cnt = 0
        one_array = ''
        for x in range(
        


"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
""" 