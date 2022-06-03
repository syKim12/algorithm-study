n = int(input())
#dp table
dp = [0]*n
#첫번째 못생긴 수는 1로 가정
dp[0] = 1

#곱하기 위한 인덱스
i2, i3, i5 = 0, 0, 0

#곱셈값
next2, next3, next5 = 2, 3, 5

for i in range(1,n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2]*2

    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3]*3

    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5
#n번재 못생긴수
print(dp[n-1])


