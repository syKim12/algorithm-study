def debug(ls):
    for l in ls[1:]:
        print(l[1:])
    #print("----------------")

n = int(input())
m = int(input())

floyd = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    floyd[i][i] = 0

for _ in range(m):
    i, j, cost = map(int, input().split())
    floyd[i][j] = min(floyd[i][j], cost)
   
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):  
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
            #print(i, j, k)
            #debug(floyd)

for i in range(1, n+1):
    result = [val if val != 1e9 else 0 for val in floyd[i]]
    print(*result[1:])