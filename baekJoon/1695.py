from collections import deque

n = int(input())
l = list(map(int, input().split()))
cnt_1, cnt_2 = 0, 0
until_num = n // 2

for back in range(n - 1, until_num - 1, -1):
    front = n - back - 1
    if l[back] == l[front]:
        continue
    else:
        cnt_1 += 1

left = deque()
right = deque()
