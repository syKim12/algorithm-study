import sys
from itertools import combinations
N = int(input())
min_difference = 1e9

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for temp_comb in combinations(range(N), N//2):
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if i in temp_comb and j in temp_comb:
                    start += arr[i][j]
                elif i not in temp_comb and j not in temp_comb:
                    link += arr[i][j]
    min_difference = min(min_difference, abs(start-link))
print(min_difference)



"""
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
"""

