def solution(wallpaper):
    files = []
    files_reverse = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                files.append((i, j))
                files_reverse.append((j, i))
    files.sort()
    files_reverse.sort()
    
    lux = files[0][0]
    luy = files_reverse[0][0]
    rux = files[-1][0] + 1 # 파일의 끝점이므로 1을 더해준다.
    ruy = files_reverse[-1][0] + 1
    answer = [lux, luy, rux, ruy]
    #print(answer)
    return answer

solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])