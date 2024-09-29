import sys
from collections import deque

sys.setrecursionlimit(10**5)

def debug(ls):
    for l in ls:
        print(l)
    return

def dfs(start_node, dist):
    for next_node, cost in tree[start_node]:
        if visited[next_node] == -1:
            visited[next_node] = dist + cost
            dfs(next_node, dist + cost)
    return
    

def main():
    global V, tree, visited
    V = int(input())
    tree = [[] for _ in range(V+1)]
    visited = [-1]*(V+1)

    # for i in range(1,V+1): -- 정점번호가 순서대로 안 들어올수도있음
    #     temp = list(map(int, sys.stdin.readline().split()))
    #     for j in range(1, len(temp)-1,2):
    #         tree[i].append((temp[j], temp[j+1]))
    for _ in range(V):
        line = list(map(int, input().split()))
        cnt_node = line[0]
        idx = 1
        while line[idx] != -1:
            adj_node, adj_cost = line[idx], line[idx+1]
            tree[cnt_node].append((adj_node, adj_cost))
            idx += 2


    visited[1] = 0
    dfs(1,0)
    
    max_dist = 0
    for i in range(1,V+1):
        if visited[i] > max_dist:
            next_node = i
            max_dist = visited[i]

    visited = [-1]*(V+1)
    visited[next_node] = 0
    dfs(next_node, 0)
    # print(visited)
    print(max(visited))

    return 


main()