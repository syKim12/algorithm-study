from collections import deque

def dfs(x,y,grad):
    global cnt
    print(x,y,grad,cnt)
    if x - 1 >= 0:
        nx = x - 1
        ny = arr[nx][1]
        n_grad = (ny - y)/(nx - x)
        if abs(grad) > abs(n_grad) and y >= ny:
            cnt += 1
            dfs(nx, ny, n_grad)
    if x + 1 < N:
        nx = x + 1
        ny = arr[nx][1]   
        n_grad = (ny - y)/(nx - x)
        if abs(grad) > abs(n_grad) and y >= ny:
            cnt += 1
            dfs(nx, ny, n_grad) 

    return cnt       
    

def bfs(x,y):
    left_q = deque()
    grad = 1e9
    left_q.append(x-1)
    cnt = 0
    while left_q:
        nx = left_q.popleft()
        if nx >= 0:
            ny = arr[nx][1]
            n_grad = (ny - y)/(nx - x)
            if grad > n_grad:
                
                cnt += 1
                #print(nx, cnt)
                grad = n_grad
            left_q.append(nx-1)

    right_q = deque()
    grad = -1e9
    right_q.append(x+1)
    while right_q:
        nx = right_q.popleft()
        if nx < N:
            ny = arr[nx][1]
            n_grad = (ny - y)/(nx - x)
            if grad < n_grad:
                
                cnt += 1
                #print(nx, ny,cnt)
                grad = n_grad
            right_q.append(nx+1)
    return cnt



def main():
    global arr, N
    
    N = int(input())
    temp = list(map(int, input().split()))
    arr = []
    max_cnt = 0
    
    for x in range(N):
        arr.append((x, temp[x]))

    for x,y in arr:
        max_cnt = max(max_cnt, bfs(x,y))

    print(max_cnt)

main()