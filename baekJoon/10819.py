N = int(input())
nlist = list(map(int, input().split()))

visited = [0]*N
candidates = []
def sol(arr,idx):
    if idx == N:
        val = 0
        for i in range(N-1):
            val += abs(arr[i] - arr[i+1])
        candidates.append(val)
        return 
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            arr.append(nlist[i])
            sol(arr, idx+1)
            visited[i] = 0
            arr.pop()

sol([], 0)
print(max(candidates))

# 6
# 20 1 15 8 4 10
# 62