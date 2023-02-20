import sys
from heapq import heappop, heappush

def debug(ls):
    for l in ls:
        print(l)
    return

city, limit, route = map(int, sys.stdin.readline().split())
arr = [[1e9*(-1)]*(city+1) for _ in range(city+1)]
limits = [[0]*(city+1) for _ in range(city+1)]

for _ in range(route):
    i, j, meal = map(int, sys.stdin.readline().split())
    arr[i][j] = max(arr[i][j], meal)

for i in range(1, city+1):
    for j in range(i, city+1):
        if limits[i-1][j] >= limit and limits[i-1][j-1] >= limit:
            continue
        elif limits[i-1][j] >= limit and limits[i-1][j-1] < limit:
            arr[i][j] += arr[i-1][j-1]
            limits[i][j] = limits[i-1][j-1] + 1
        elif limits[i-1][j] < limit and limits[i-1][j-1] >= limit:
            arr[i][j] = arr[i-1][j]
            limits[i][j] = limits[i-1][j] + 1
        else:
            if arr[i-1][j] > arr[i][j] + arr[i-1][j-1]:
                arr[i][j] = arr[i-1][j]
                limits[i][j] = limits[i-1][j] + 1
            else:
                arr[i][j] += arr[i-1][j-1]
                limits[i][j] = limits[i-1][j-1] + 1

#print(arr[-1][-1]+1e9)
#print(arr[-1][-1])
#print(arr)
val = int(arr[-1][-1] + 1e9)
print(val)

# test case example
# 3 3 2
# 1 2 3
# 1 3 1
# answer: 1



"""
# used dijkstra
def dijkstra(start):
    global limit
    meals = [0]*(city+1)
    q = []
    heappush(q, (0, start))
    while q:
        meal, num = heappop(q)
        if meals[num] < meal:
            continue
        if limit < 0:
            break
        for i in graph[num]:
            value = meal + i[1]
            if value < meals[i[0]] and limit > 0:
                meals[i[0]] = value
                limit -= 1
                heappush(q, (value, i[0]))
    return meals

city, limit, route = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(city+1)]

for _ in range(route):
    i, j, meal = map(int, sys.stdin.readline().split())
    graph[i].append((j, meal*(-1)))

meals = dijkstra(1)
print(meals[-1]*(-1))
"""