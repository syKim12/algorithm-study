import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
home, chicken = [], []
# 입력 받기
for i in range(1,n+1):
    temp = [0] + list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))


comb = list(combinations(chicken, m))
min_city_dist = 1e9

for l in comb: #combination 안에 있는 것을 기준으로 최소값 찾아야하므로 comb 부터 탐색 
    city_dist = 0
    for i, j in home: # 각각의 집들에서 최소거리 찾아야하므로 home 부터 탐색
        min_dist = 1e9
        for z in range(m): # 각 집마다 치킨집까지의 최소 거리 탐색
            x, y = l[z][0], l[z][1]
            #print(i, j, x, y)
            dist = abs(i-x) + abs(j-y)
            min_dist = min(dist, min_dist)
        #print(min_dist)
        city_dist += min_dist
    min_city_dist = min(min_city_dist, city_dist)

print(min_city_dist)