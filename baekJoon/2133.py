N = int(input())
if N % 2 == 1: # 홀수
    print(0)
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
