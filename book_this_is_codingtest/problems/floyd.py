#n이 100 이하이므로 floyd warshall 이용

INF = int(1e9)
#도시 개수
n = int(input())
#버스 (간선) 개수
m = int(input())
#2차원 리스트 생성
graph = [[INF] * (n+1) for _ in range(n+1)]
#자기 자신에서 자기 자신으로 가면 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
#각 간선 정보 설정
for i in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()