N = int(input())
cnt = 0
row = [0]*N

def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x]-row[i]) == (x-i):
            return False
    return True

def sol(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        row[x] = i
        if check(row):
            sol(x+1)

sol(0)
print(cnt)


"""
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
"""