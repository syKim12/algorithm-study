from collections import deque

def ice(d, s):

def move():
    # 아래, 오른쪽, 위, 왼쪽 으로 이동
    ddx = []
    ddy = 
    start_x, start_y =     


n, m = map(int, input().split())
array = []
dx = ["None", -1, 1, 0, 0]
dy = ["None", 0, 0, -1, 1]
s_x, s_y = (n-1)/2, (n-1)/2 # shark
able_array = [[0]*n for _ in range(n)]


for _ in range(n):
    array.append(list(map(int, input().split())))

for _ in range(m):
    d, s = map(int, input().split())    