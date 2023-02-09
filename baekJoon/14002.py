import sys

N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
dp = [1]*(N+1)
for i in range(N):
    for j in range(i):
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

max_value = max(dp)
result = []
for i in range(N-1, -1, -1):
    if dp[i] == max_value:
        result.append(nlist[i])
        max_value -= 1
result.reverse()
print(*result)



"""
N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
answer = []
max_length = 0
max_list = [0]
for i in range(N):
    temp = [0]
    for k in range(i, N):
        if temp[-1] < nlist[k]:
            temp.append(nlist[k])
    answer.append(temp[1:])
for l in answer:
    if len(l) >= max_length:
        max_length = len(l) 
        max_list = l
print(max_length)
print(*max_list)
"""