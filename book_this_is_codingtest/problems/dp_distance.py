str1 = input()
str2 = input()

#스트링 길이
n = len(str1)
m = len(str2)
#dp 테이블 초기 설정
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        #문자가 같다면
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        #문자가 다르다면
        else:
            #삽입은 왼쪽에서, 교체는 왼쪽 위에서, 삭제는 위에서 아래로
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])


print(dp[n][m])