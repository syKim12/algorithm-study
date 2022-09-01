from collections import deque

def solution(maps):
    answer = 0

    q = deque()
    q.append([0, 0, 0])
    while q:
        n, m, cnt = q.popleft()
    return answer