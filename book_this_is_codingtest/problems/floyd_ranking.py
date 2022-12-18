INF = 1e9
#n은 학생 수, m은 간선 수
n, m = map(int, input().split())

#그래프 설정
graph = [[INF]*(n+1) for _ in range(n+1)]
#그래프 초기값 설정
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)

