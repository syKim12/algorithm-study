import sys
from collections import deque

house, router = map(int, sys.stdin.readline().split())
distance = 0
houses = [int(sys.stdin.readline()) for _ in range(house)]
#for i in range(house):
#    houses[i] = int(input())
houses.sort()

start = 1
end = houses[-1] - houses[0]
max_gap = 0

while start <= end:
    gap = (start+end) // 2
    idx, cnt = houses[0], 1
    for i in range(1, house):
        if houses[i] >= idx + gap:
            idx = houses[i]
            cnt += 1
    if cnt >= router:
        start = gap + 1
        max_gap = gap
    else:
        end = gap - 1

print(max_gap)
