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




"""
for k in range(3, div+1):
    flag_unique = True
    for i in range(1, k):
        for j in range(k-1, 0, -1):
            if i + j == k:
                if flag_unique:
                    flag_unique = False
                    dp[k] += dp[i]*dp[j]
                else:
                    dp[k] += dp[j]*2
    dp[k] += 2
print(dp[-1])
"""
"""    
elif N == 2:
    print(3)
elif N == 4:
    print(11)
else:
    div = N // 2 
    dp = [0]*(div+1)
    dp[1], dp[2] = 3, 11
    flag = True
    for i in range(1, div+1):
        for j in range(div, 0, -1):
            if i + j == div:
                if flag:
                    dp[div] += dp[i]*dp[j]
                else:
                    dp[div] = dp[i]*dp[j]*2+2
    #print(dp)
    print(dp[div])
"""