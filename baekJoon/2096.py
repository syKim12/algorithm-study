import sys

N = int(input())
# 첫번째 행의 값 받기
dp_max = list(map(int, sys.stdin.readline().split()))
dp_min = dp_max.copy()
# 두번째 행부터 계산
for _ in range(1,N):
    now = list(map(int, sys.stdin.readline().split()))
    prev_max, prev_min = dp_max.copy(), dp_min.copy() # 이전 값을 보존하기 위해 copy함
    for j in range(3): # 열은 세개로 고정
        if j == 0: # 첫번째 열
            dp_max[j] = now[j] + max(prev_max[j], prev_max[j+1])
            dp_min[j] = now[j] + min(prev_min[j], prev_min[j+1])
        elif j == 2: # 세번째 열
            dp_max[j] = now[j] + max(prev_max[j-1], prev_max[j])
            dp_min[j] = now[j] + min(prev_min[j-1], prev_min[j])
        else: # 두번째 열
            dp_max[j] = now[j] + max(prev_max[j-1], prev_max[j], prev_max[j+1])
            dp_min[j] = now[j] + min(prev_min[j-1], prev_min[j], prev_min[j+1])
print(max(dp_max), min(dp_min))
"""
dp_max = [[0] * N for _ in range(N)]
dp_min = [[0] * N for _ in range(N)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        dp_max[i][j], dp_min[i][j] = temp[j], temp[j]

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp_max[i][j] += max(dp_max[i-1][j], dp_max[i-1][j+1])
            dp_min[i][j] += min(dp_min[i-1][j], dp_min[i-1][j+1])
        elif j == N-1:
            dp_max[i][j] += max(dp_max[i-1][j-1], dp_max[i-1][j])
            dp_min[i][j] += min(dp_min[i-1][j-1], dp_min[i-1][j])
        else:
            dp_max[i][j] += max(dp_max[i-1][j-1], dp_max[i-1][j], dp_max[i-1][j+1])
            dp_min[i][j] += min(dp_min[i-1][j-1], dp_min[i-1][j], dp_min[i-1][j+1])
       
print(max(dp_max[-1]), min(dp_min[-1]))
"""