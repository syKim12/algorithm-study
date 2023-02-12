import sys

N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
reverse_nlist = nlist[::-1]
increasing = [1]*N
decreasing = [1]*N

for i in range(N):
    for j in range(i):
        if nlist[i] > nlist[j]:
            increasing[i] = max(increasing[i], increasing[j]+1)
        if reverse_nlist[i] > reverse_nlist[j]:
            decreasing[i] = max(decreasing[i], decreasing[j]+1)
"""
for i in range(N):
    temp_max = -1
    index = -1
    for j in range(i):
        if nlist[i] > nlist[j] and nlist[j] >= temp_max:
            temp_max = nlist[j]
            index = j
    if index >= 0:
        increasing[i] = increasing[index] + 1

for i in range(N-1, -1, -1):
    temp_max = 0
    index = -1
    for j in range(N-1, i, -1):
        if nlist[i] > nlist[j] and nlist[j] >= temp_max:
            temp_max = nlist[j]
            index = j
    if index >= 0:
        decreasing[i] = decreasing[index] + 1
"""
#print(increasing)
#print(decreasing)
lis = [increasing[i]+decreasing[N-i-1]-1 for i in range(N)]
print(max(lis))