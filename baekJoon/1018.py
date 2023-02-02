import sys

check_w = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
        ]
check_b = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
        ]

N, M = map(int, sys.stdin.readline().split())
arr = [0]*N 
visited = [[0]*M for _ in range(N)]
candidates = []
for i in range(N):
    arr[i] = sys.stdin.readline().strip()
min_cnt = 1e9

for i in range(0, N-7): #세로
    for j in range(0, M-7):#가로
        cnt = 0
        #BWBW로 시작했을 때, WBWB로 시작할 때 두 경우로 비교
        for m in range(i, i+8): 
            for n in range(8): 
                    if arr[m][j+n] != check_w[m-i][n]:
                        cnt += 1                
        min_cnt = min(cnt, min_cnt)
        cnt = 0
        for m in range(i, i+8): 
            for n in range(8): 
                    if arr[m][j+n] != check_b[m-i][n]:
                        cnt += 1  
        min_cnt = min(cnt, min_cnt)
print(min_cnt)    
        