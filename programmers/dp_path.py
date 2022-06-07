"""
def solution(m, n, puddles):
    answer = 0
    INF = 1e9
    dp = [[INF] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 0
                continue
            left = dp[i - 1][j]
            up = dp[i][j - 1]
            # avoid puddles
            for puddle in puddles:
                if j == puddle[0] and i == puddle[1]:
                    up, left = INF, INF
                    continue
            dp[i][j] = 1 + min(up, left)
    answer = (dp[n][m] - 1) % (1000000007)
    print(dp)
    return answer
"""
def solution(m, n, puddles):
    answer = 0
    INF = 1e9
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            left = dp[i - 1][j]
            up = dp[i][j - 1]
            # avoid puddles
            for puddle in puddles:
                if j == puddle[0] and i == puddle[1]:
                    up, left = 0, 0
                    continue
            dp[i][j] = left + up
    print(dp)
    answer = dp[n][m] % (1000000007)
    return answer


print(solution(5, 4, [[3, 2]]))