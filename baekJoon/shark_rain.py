from collections import deque

#def move_cloud():

def get_direction(x, y, move_x, move_y):
    temp_x = x + move_x
    temp_y = y + move_y
    # get row number
    nx = temp_x % n 
    if nx == 0:
        nx = n  
    # get column number
    ny = temp_y % n
    if ny == 0:
        ny = n
    return nx, ny

def print_coluds(clouds):
    for cloud in clouds:
        print(cloud)
    #print('-----------------')

def copy_cloud(x, y):
    cnt = 0
    diagonal_x = [-1, 1, -1, 1]
    diagonal_y = [-1, -1, 1, 1]
    for i in range(4):
        nx = x + diagonal_x[i]
        ny = y + diagonal_y[i]
        if 1 <= nx <= n and 1 <= ny <= n:
            if array[nx][ny] > 0:
                cnt += 1
    return cnt


n, m = map(int, input().split())
array = [[0] * (n + 1)]
cloud = [[0]*(n + 1) for _ in range(n + 1)]
cloud[n][1], cloud[n][2], cloud[n-1][1], cloud[n-1][2] = 1, 1, 1, 1
dx = ["None", 0, -1, -1, -1, 0, 1, 1, 1]
dy = ["None", -1, -1, 0, 1, 1, 1, 0, -1]

for r in range(n):
    array.append(list(map(int, input().split())))
    array[-1].insert(0, 0)    



for _ in range(m):
    d, s = map(int, input().split())
    cloud_visited = [[0]*(n + 1) for _ in range(n + 1)]
    # move cloud and make it rain
    move_x = dx[d]*s
    move_y = dy[d]*s
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if cloud[r][c] > 0:
                # move cloud 
                nx, ny = get_direction(r, c, move_x, move_y)
                #print("nx, ny: ",nx, ny)
                cloud_visited[nx][ny]= 1
                # rain and cloud disappear
                array[nx][ny] += 1
                cloud[r][c] = 0
                #cloud[nx][ny] = 1 # to check if it rained
    #print_coluds(array)
    # copy rain
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if cloud_visited[r][c] > 0:
                #cloud[r][c] = 0 # since clouds must have been deleted
                d_rain = copy_cloud(r, c)
                array[r][c] += d_rain
    #print_coluds(array)         
    #make cloud
    # print(1, cloud_visited)
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            # print(cloud_visited[r][r], not cloud_visited[r][c])
            if (cloud_visited[r][c] == 0) and (array[r][c] >= 2):
                cloud[r][c] = 1
                array[r][c] -= 2
    #print_coluds(array)
    # print(cloud)
    # print(cloud_visited)
    #print(array) 
    #print("**********")           

rain = 0
for r in range(1, n + 1):
    for c in range(1, n + 1):
        rain += array[r][c]
print(rain)

    


