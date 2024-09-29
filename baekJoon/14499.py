

def debug(ls):
    print('########')
    for l in ls:
        print(l)
    
    return

def check(x,y,dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < r and 0 <= ny < c:
        return True
    return False

def turn(x, y, dir):
    global dice
    temp_dice = {k: v for k, v in dice.items()}
    if dir == 1:
        dice[(1,0)] = temp_dice[(3,1)]
        dice[(1,1)] = temp_dice[(1,0)]
        dice[(1,2)] = temp_dice[(1,1)]
        dice[(3,1)] = temp_dice[(1,2)]
    elif dir == 2:
        dice[(1,0)] = temp_dice[(1,1)]
        dice[(1,1)] = temp_dice[(1,2)]
        dice[(1,2)] = temp_dice[(3,1)]
        dice[(3,1)] = temp_dice[(1,0)]
    elif dir == 4:
        dice[(0,1)] = temp_dice[(1,1)]
        dice[(1,1)] = temp_dice[(2,1)]
        dice[(2,1)] = temp_dice[(3,1)]
        dice[(3,1)] = temp_dice[(0,1)]
    elif dir == 3:
        dice[(0,1)] = temp_dice[(3,1)]
        dice[(1,1)] = temp_dice[(0,1)]
        dice[(2,1)] = temp_dice[(1,1)]
        dice[(3,1)] = temp_dice[(2,1)]

    nx, ny = x + dx[dir], y + dy[dir]

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[(3,1)]
    else:
        dice[(3,1)] = arr[nx][ny]
        arr[nx][ny] = 0
    return nx, ny

def main():
    global r, c, arr, dice, dx, dy
    r, c, d_x, d_y, command = map(int, input().split())
    arr = []
    dice = {(0,1):0, (1,0):0, (1,1):0, (1,2):0, (2,1):0, (3,1):0}
    dx = [0, 0, 0, -1, 1] # 동서남북의 숫자(1,2,3,4)를 맞추기 위해 앞에 0 추가.
    dy = [0, 1, -1, 0, 0]

    for i in range(r):
        temp = list(map(int, input().split()))
        arr.append(temp)
    order = list(map(int, input().split()))
    for o in order:
        if check(d_x, d_y, o): 
            d_x, d_y = turn(d_x, d_y, o)
            print(dice[(1,1)])


    return

main()