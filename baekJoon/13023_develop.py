import sys
from collections import deque

def debug(ls):
    for l in ls:
        print(l)
    print("##############")
    return

def dfs(n, cnt):
    val = 0
    for node in tree[n]:
        if not visited[node]:
            #print(n, visited, cnt, 'val: ', val)
            if cnt == 4:
                return 1
            visited[node] = 1
            val = dfs(node, cnt + 1)
            if val:
                return val
            visited[node] = 0
    return val

def main():
    global tree, visited
    ppl, friends = map(int, input().split())
    tree = [[] for _ in range(ppl)]

    for _ in range(friends):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    for p in range(ppl):
        visited = [0] * ppl
        visited[p] = 1
        if bfs(p):
            return 1

    return 0

print(main())