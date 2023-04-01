import sys

def debug(ls):
    for l in ls:
        print(l)
    print("****************")
    return          

def main():
    out_sand = 0
    turn = 2
    move_dist = 0
    curl = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    proportion0 = [[0, 0, 0.02, 0, 0],[0, 0.1, 0.07, 0.01, 0],[0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
    proportion1 = [[0, 0, 0, 0, 0], [0, 0.01, 0, 0.01, 0], [0.02, 0.07, 0, 0.07, 0.02], [0, 0.1, 0, 0.1, 0], [0, 0, 0.05, 0, 0]]
    proportion2 = [[0, 0, 0.02, 0, 0], [0, 0.01, 0.07, 0.1, 0], [0, 0, 0, 0, 0.05],[0, 0.01, 0.07, 0.1, 0],[0, 0, 0.02, 0, 0]]
    proportion3 = [[0, 0, 0.05, 0, 0],[0, 0.1, 0, 0.1, 0],[0.02, 0.07, 0, 0.07, 0.02],[0, 0.01, 0, 0.01, 0],[0, 0, 0, 0, 0]]
    proportions = {0: proportion0, 1: proportion1, 2: proportion2, 3: proportion3}
    tornado_r, tornado_c = N // 2, N // 2
    proportion = proportions[0]

    while not (tornado_r == 0 and tornado_c == 0):
        # move sand
        tornado_r, tornado_c = tornado_r + dx[curl], tornado_c + dy[curl]
        #print(tornado_r, tornado_c, curl)
        proportion = proportions[curl]
        move_dist += 1
        move_sand = arr[tornado_r][tornado_c]
        arr[tornado_r][tornado_c] = 0
        left = move_sand
        for i in range(5):
            for j in range(5):
                x, y = tornado_r + i - 2, tornado_c + j - 2
                now_sand = int(move_sand * proportion[i][j])
                left -= now_sand
                # when out of range
                if x < 0 or x >= N or y < 0 or y >= N:
                    out_sand += now_sand
                else:
                    arr[x][y] += now_sand
        # move sand to alpha
        alpha_r, alpha_c = tornado_r + dx[curl], tornado_c + dy[curl]
        #print(alpha_r, alpha_c)
        if alpha_r < 0 or alpha_r >= N or alpha_c < 0 or alpha_c >= N:
            out_sand += left
        else:
            arr[alpha_r][alpha_c] += left

        
        #move_dist, turn, curl = turn(move_dist, turn, proportions)
        if move_dist == turn // 2 or move_dist == turn:
            curl = (curl + 1) % 4
            #proportion = proportions[curl]
            if move_dist == turn:
                move_dist = 0
                turn += 2
        #debug(arr)
    return out_sand

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#debug(arr)
print(main())