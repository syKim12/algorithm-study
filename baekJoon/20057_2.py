import sys

def debug(l):
    print("################")
    for i in l:
        print(i)

sand = [[[0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]],
        [[0, 0, 0, 0, 0],
         [0, 0.01, 0, 0.01, 0],
         [0.02, 0.07, 0, 0.07, 0.02],
         [0, 0.1, 0, 0.1, 0],
         [0, 0, 0.05, 0, 0]],
         [[0, 0, 0.02, 0, 0],
          [0, 0.01, 0.07, 0.1, 0],
          [0, 0, 0, 0, 0.05],
          [0, 0.01, 0.07, 0.1, 0],
          [0, 0, 0.02, 0, 0]],
          [[0, 0, 0.05, 0, 0],
           [0, 0.1, 0, 0.1, 0],
           [0.02, 0.07, 0, 0.07, 0.02],
           [0, 0.01, 0, 0.01, 0],
           [0, 0, 0, 0, 0]]]


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = N//2, N//2
dir = 0
out_sand = 0
cnt = 0
flag = 0 # 루프 탈출
for move in range(1, N+1):
    for _ in range(2):
        for m in range(move):
            dir = dir % 4
            center_x, center_y = x + dx[dir], y + dy[dir]
            if center_x == 0 and center_y == 0:
                flag = 1
                
            if arr[center_x][center_y] > 0:
                center_sand = arr[center_x][center_y]
                current_sand = 0

                for i in range(-2, 3):
                    for j in range(-2, 3):
                        nx, ny = center_x + i, center_y + j
                        
                        temp_sand = int(center_sand * sand[dir][i+2][j+2])
                        
                        current_sand += temp_sand

                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += temp_sand
                            
                        else:
                            out_sand += temp_sand
                ax, ay = center_x + dx[dir], center_y + dy[dir]
                if 0 <= ax < N and 0 <= ay < N:
                    arr[ax][ay] += (center_sand - current_sand) # 남은 모래
                else:
                    out_sand += (center_sand - current_sand)
                arr[center_x][center_y] = 0
            x = center_x
            y = center_y
            #print(center_x, center_y)
            #debug(arr)
            #print(out_sand)
            if flag:
                break
        dir += 1
        if flag:
            break
  
print(out_sand)

