import sys, heapq

def dijkstra(hacked, computer, graph):
    second = [1e9]*(computer+1)
    visited = [0]*(computer+1)
    q = []
    heapq.heappush(q, (0, hacked))
    second[hacked] = 0
    while q:
        sec, num = heapq.heappop(q)
        if second[num] < sec:
            continue
        for i in graph[num]:
            value = sec + i[1]
            if value < second[i[0]]:
                second[i[0]] = value
                heapq.heappush(q, (value, i[0]))
    hacked_computer, hacked_time = 0, 0
    for i in range(1, computer+1):
        if second[i] != 1e9:
            hacked_computer += 1
            hacked_time = max(hacked_time, second[i])
    return hacked_computer, hacked_time
        

test_case = int(input())
for _ in range(test_case):
    computer, dependency, hacked = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(computer+1)]
    for _ in range(dependency):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s)) 
    hacked_computer, hacked_time = dijkstra(hacked, computer, graph)  
    print(hacked_computer, hacked_time)  
