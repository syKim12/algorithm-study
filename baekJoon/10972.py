N = int(input())
nlist = list(map(int, input().split()))

for i in range(N):
    if nlist[i] == N:
        N_idx = i

if N_idx == 0:
    print(-1)
else:
    for i in range(N-1, 0, -1):
        if nlist[N_idx-1] < nlist[i]:
            nlist[N_idx-1], nlist[i] = nlist[i], nlist[N_idx-1]
            break
    for n in nlist:
        print(n, end=' ')

"""
while True:
    if N_idx == 0:
        print(nlist)
        break
    for i in range(N-1, 0, -1):
        if nlist[N_idx-1] < nlist[i]:
            nlist[N_idx-1], nlist[i] = nlist[i], nlist[N_idx-1]
"""

# 13542 -> 14532