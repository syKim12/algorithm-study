import sys
from itertools import combinations
N = int(input())
min_difference = 1e9

arr = [[0]*20 for _ in range(20)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        arr[i][j] = temp[j]

numlist = [i for i in range(N)]
numset = set(numlist)
visited = [0]*N

def sol(start_path, visited, end):
    global numset
    if len(start_path) == end:
        link_path = numset - start_path
        comparison(start_path, link_path)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            start_path.add(i)
            sol(start_path, visited, end)
            start_path.remove(i)
            visited[i] = 0

def comparison(start, link):
    global min_difference
    start_list = list(start)
    link_list = list(link)
    start_c = combinations(start_list, 2)
    link_c = combinations(link_list, 2)
    start_score = 0
    link_score = 0
    for i, j in start_c:
        start_score += arr[i][j]
        start_score += arr[j][i]
    for i, j in link_c:
        link_score += arr[i][j]
        link_score += arr[j][i]        
    difference = abs(start_score - link_score)
    min_difference = min(difference, min_difference)
    return

s = set()
sol(s, visited, N/2)
print(min_difference)

"""
def readInt():
    return int(stdin.readline())

'''
Begin solution
'''

from itertools import combinations
n = readInt()
grid = [list(map(int, read().split())) for _ in range(n)]

diff = 100 * n
for combo in combinations(range(n), n // 2):
    s1 = 0  # in combo
    s2 = 0
    for i in range(n):
        for j in range(n):
            if i in combo and j in combo:
                s1 += grid[i][j]
            elif i not in combo and j not in combo:
                s2 += grid[i][j]

    diff = min(diff, abs(s1 - s2))

print(diff)
"""