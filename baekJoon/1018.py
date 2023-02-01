import sys

def make_board(color):
    if color == "W":
        check_board = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
        ]
    else:
        check_board = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
        ]
    return check_board

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
        check = make_board(arr[i][j])
        print(check)
        for m in range(i, i+8): 
            print(arr[m][j:j+8])
            for n in range(8): 
                if m <= 7:
                    if arr[m][j+n] != check[m][n]:
                        cnt += 1   
                else:
                    if arr[m][j+n] != check[(m][n]:
                        cnt += 1 
        min_cnt = min(cnt, min_cnt)
        print("----------", min_cnt, cnt, m, j)
print(min_cnt)    
        
# 10 10 케이스