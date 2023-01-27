N = int(input())
nlist = list(map(int, input().split()))

find = False
for i in range(N-1, 0, -1):
    if m[i-1] < m[i]:  # 뒷 값이 앞 값보다 크다면
        for j in range(N-1, 0, -1):
            if m[i-1] < m[j]:
                m[i-1], m[j] = m[j], m[i-1]  # 간단한 스왑
                m = m[:i] + sorted(m[i:])  # 이 부분 떄문에 헤맴
                find = True
                break
    if find:
        print(*m)  # 리스트 앞에 *를 붙이면 안에 있는 숫자들을 1 2 3 4 이런 식으로 출력할 수 있음
        break
if not find:
    print(-1)

"""
def sol(N, nlist):
    def swap(N_idx, nlist):
        for i in range(N-1, 0, -1):
            if nlist[N_idx-1] < nlist[i]:
                
                nlist[N_idx-1], nlist[i] = nlist[i], nlist[N_idx-1]
                nlist = nlist[:N_idx] + sorted(nlist[N_idx:])
                break
        for n in nlist:
                print(n, end=' ')
        return
            
    for i in range(N):
        if nlist[i] == N:
            N_idx = i
    if N_idx == 0:
        check = N - 1
        for i in range(1, N):
            if nlist[i] != check:
                swap(i+1, nlist)
                return
            check -= 1
        print(-1)
        return
    else:
        swap(N_idx, nlist)

sol(N, nlist)
"""

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