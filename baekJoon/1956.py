v, e = map(int, input().split())
floyd = [[1e9]*(v+1) for _ in range(v+1)]

for _ in range(e):
    i, j, dist = map(int, input().split())
    floyd[i][j] = dist

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
#print(floyd)
dist_list = [floyd[i][i] for i in range(1, v+1)]
min_dist = min(dist_list) 
if min_dist == 1e9:
    print(-1)
else:
    print(min_dist)