#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
sys.setrecursionlimit(5000)
from collections import deque

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
def dfs2(start, end, cost):
    global visited, costs, graph
    if start == end:
        costs.append(cost)
        return
    for n, c in graph[start]:
        if not visited[n]:
           visited[n] = 1
           dfs(n, end, max(cost, c))
           visited[n] = 0
    return
    
def dfs(start, end, cost):
    global visited, costs, graph, best_cost
    if start == end:
        costs.append(cost)
        best_cost = min(best_cost, cost)  # Update best_cost when a path completes
        return
    visited[start] = True
    for n, c in graph[start]:
        if not visited[n]:
            new_cost = max(cost, c)
            if new_cost < best_cost:  # Pruning condition
                dfs(n, end, new_cost)
    visited[start] = False
    return
def bfs(end):
    global visited, costs, graph
    q=deque() 
    q.append(([1],0))
    while q:
        path, c = q.popleft()
        if path[-1] == end:
            costs.append(c)
            
        for n, temp_c in graph[path[-1]]:
            if n not in path:
                q.append((path+[n], max(temp_c, c)))
    return costs
                
def dijkstra2(start,end):
    global visited, graph
    q=[(0,start)]
    while q:
        c, n = heapq.heappop(q)

def dijkstra(end):
    global graph, g_weight
    distances = [1e9]*(end+1)
    start = 1
    priority_queue = [(0, start, 0)]
    visited = [0]*(end+1) 
    max_cost = [0]*(end+1)
    result = 0
    while priority_queue:
        current_distance, current_node, current_max_cost = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = 1 

        for adjacent, weight in graph[current_node]:
            if not visited[adjacent]:
                distance = current_distance + weight
                temp = max(current_max_cost, weight)
                if distance < distances[adjacent] or (distance == distances[adjacent] and temp < max_cost[adjacent]):
                    
                    #print(current_node, adjacent, current_max_cost)
                    distances[adjacent] = distance
                    
                    max_cost[adjacent] = temp
                    heapq.heappush(priority_queue, (distance, adjacent, temp))
    #print(distances, cost)
    return max_cost[end]

def getCost(g_nodes, g_from, g_to, g_weight):
    global visited, costs, graph, best_cost
    # Print your answer within the function and return nothing
    graph = [[] for _ in range(g_nodes+1)]
    visited = [0]*(g_nodes+1)
    costs = []
    best_cost = 1e9
   # graph.sort(key=lambda x: x[2])
    for i in range(len(g_from)):
        graph[g_from[i]].append((g_to[i], g_weight[i]))
        graph[g_to[i]].append((g_from[i], g_weight[i]))
    
    #graph.sort(key=lambda x: x[1])
    visited[1] = 1
    #dfs(1, g_nodes, 0)
    #print(min(costs))
    
    print(dijkstra(g_nodes))
    return
    

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
