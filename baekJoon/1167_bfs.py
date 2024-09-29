import sys
from collections import deque

def debug(ls):
    for l in ls:
        print(l)
    return

def bfs(start_node, dist):
    q = deque()
    q.append((start_node, dist))
    while q:
        node, dist = q.popleft()
        for adj, cost in tree[node]:
            if visited[adj] == -1:
                visited[adj] = cost + dist
                q.append((adj, cost + dist))

    return
    

def main():
    global V, tree, visited
    V = int(input())
    tree = [[] for _ in range(V+1)]
    visited = [-1]*(V+1)

    for _ in range(V):
        line = list(map(int, input().split()))
        cnt_node = line[0]
        idx = 1
        while line[idx] != -1:
            adj_node, adj_cost = line[idx], line[idx+1]
            tree[cnt_node].append((adj_node, adj_cost))
            idx += 2


    visited[1] = 0
    bfs(1,0)
    
    max_dist = 0
    for i in range(1,V+1):
        if visited[i] > max_dist:
            next_node = i
            max_dist = visited[i]

    visited = [-1]*(V+1)
    visited[next_node] = 0
    bfs(next_node, 0)
    # print(visited)
    print(max(visited))

    return 


main()