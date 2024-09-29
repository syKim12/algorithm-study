import sys

def debug(ls):
    for l in ls:
        print(l)
    print("##############")
    return

def dfs(n, visited, cnt):
    val = 0
    for node in tree[n]:
        if not visited[node]:
            #print(n, visited, cnt, 'val: ', val)
            if cnt == 4:
                return 1
            temp_visited = visited[:]
            temp_visited[node] = 1
            val = dfs(node, temp_visited, cnt + 1)
            if val:
                return val
    
    return val

def main():
    global tree
    ppl, friends = map(int, input().split())
    tree = [[] for _ in range(ppl)]

    for _ in range(friends):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    for p in range(ppl):
        visited = [0] * ppl
        visited[p] = 1
        if dfs(p, visited, 1):
            return 1

    return 0

print(main())