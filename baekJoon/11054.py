import sys

N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
reverse_nlist = nlist[::-1]
increasing = [1]*N
decreasing = [1]*N

# 348ms
for i in range(N):
    for j in range(i):
        if nlist[i] > nlist[j]:
            increasing[i] = max(increasing[i], increasing[j]+1)
        if nlist[N-i-1] > nlist[N-j-1]:
            decreasing[N-i-1] = max(decreasing[N-i-1], decreasing[N-j-1]+1)
# 268ms
"""
for i in range(N):
    for j in range(i):
        if nlist[i] > nlist[j]:
            increasing[i] = max(increasing[i], increasing[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if nlist[i] > nlist[j]:
            decreasing[i] = max(decreasing[i], decreasing[j]+1) 
"""       
"""
for i in range(N):
    for j in range(i):
        if nlist[i] > nlist[j]:
            increasing[i] = max(increasing[i], increasing[j]+1)
        if reverse_nlist[i] > reverse_nlist[j]:
            decreasing[i] = max(decreasing[i], decreasing[j]+1)
"""

#print(increasing)
#print(decreasing)
#lis = [increasing[i]+decreasing[N-i-1]-1 for i in range(N)]
lis = [increasing[i]+decreasing[i]-1 for i in range(N)]
print(increasing)
print(decreasing)
print(lis)