def solution(N, road, K):
    answer = 0
    INF = 1e9
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    # 자기 자신으로 가는 것은 초기화
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0

    # 간선 정보 입력
    for r in road:
        a, b, c = map(int, r)
        # 같은 노드를 연결하는 길이가 다른 간선이 있을수도 있으므로 최솟값을 넣어야함
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    # floyd warshall

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    for b in range(1, N + 1):
        if graph[1][b] <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))