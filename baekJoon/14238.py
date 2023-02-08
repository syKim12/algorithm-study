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
#perm = list(permutations(record, len(record)))
visited = [0]*len(record)
dfs(0, [])
if not flag:
    print(-1)
# permutation 때문에 메모리 초괴..?
