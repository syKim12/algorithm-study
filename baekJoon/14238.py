from sys import stdin


def dfs(a, b, c, prev):

    # a, b, c의 개수가 초기 카운트와 같으면 찾은 것
    if [a, b, c] == cnt:
        print(''.join(answer))
        exit(0)

    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    dp[a][b][c][prev[0]][prev[1]] = True

    # A개수 만큼 사용하지 않았다면
    if a + 1 <= cnt[A]:
        answer[a + b + c] = 'A'
        if dfs(a + 1, b, c, [prev[1], A]):
            return True
    # B개수 만큼 사용하지 않았다면
    if b + 1 <= cnt[B]:
        answer[a + b + c] = 'B'
        # 전날에 선택한 것이 B가 아니라면
        if prev[1] != B:
            if dfs(a, b + 1, c, [prev[1], B]):
                return True
    # C개수 만큼 사용하지 않았다면
    if c + 1 <= cnt[C]:
        answer[a + b + c] = 'C'
        # 전전날과 전날에 선택한 것이 C가 아니라면
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c + 1, [prev[1], C]):
                return True
    return False


if __name__ == '__main__':
    A, B, C = 0, 1, 2
    s = list(stdin.readline().rstrip())
    length = len(s)
    answer = [''] * length
    # a, b, c 개수 카운트.
    cnt = [s.count(word) for word in ('A', 'B', 'C')]
    dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]
    dfs(0, 0, 0, [0, 0])
    print(-1)

"""
from itertools import permutations
import sys

def check(path):
    global record
    flag = 1
    for i in range(len(path)-1):
        if path[i] == 'B':
            if path[i+1] == 'B':
                flag = 0
                break
        elif i < len(record)-2 and path[i] == 'C':
            if path[i+1] == 'C' and path[i+2] == 'C':
                flag = 0
                break
    if flag:
        print(*path, sep='')
        return 1
    return 0

def dfs(idx, path):
    global record, visited, flag
    if len(path) == len(record):
        flag = check(path)
        return
    for i in range(len(record)):
        if not visited[i]:
            visited[i] = 1
            path.append(record[i])
            dfs(i+1,path)
            if flag:
                return
            visited[i] = 0
            path.pop()
    return



record = [s for s in input()]
visited = [0]*len(record)
dfs(0, [])
if not flag:
    print(-1)
"""