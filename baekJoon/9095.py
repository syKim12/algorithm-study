
"""
for _ in range(N):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(n+1):
        for j in range(n+1):
            temp = n - (i + 2*j)
            print(i, j)
            if temp >= 0:
                check_3 = temp % 3
                if check_3 == 0:
                    print(i, j, temp)
                    cnt += 1
    print(cnt)
"""
import sys

N = int(sys.stdin.readline())
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)

for _ in range(N):
    n = int(input())
    print(sol(n))

# 브루트포스
cnt = 0
