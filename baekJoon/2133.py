N = int(input())
if N % 2 == 1: # 홀수
    print(0)
    exit(0)
elif N == 2:
    print(3)
    exit(0)
elif N == 4:
    print(11)
    exit(0)
div = N // 2
dp = [0]*(div+1)

dp[1], dp[2] = 3, 11


for k in range(3, div+1):
    flag_unique = True
    for i in range(1, div):
        if flag_unique:
            flag_unique = False
            dp[k] += dp[i]*dp[k-i]
        else:
            dp[k] += dp[k-i]*2
    dp[k] += 2
#print(dp)
print(dp[-1])

