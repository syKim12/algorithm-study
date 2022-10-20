from collections import deque

n = int(input())
l = list(map(int, input().split()))
cnt = 0

q = deque(l)
while True:
    if len(q) <= 1:
        break
    left = q.popleft()
    right = q.pop()
    if left != right:
        q.appendleft(left)
        q.append(right)
        q.append(left)
        cnt += 1

print(cnt)