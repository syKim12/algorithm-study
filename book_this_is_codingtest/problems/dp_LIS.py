#LIS 참고 https://chanhuiseok.github.io/posts/algo-49/

n = int(input())
array = list(map(int, input().split()))

#순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array. reverse()

#dp를 위한 1차원 dp 테이블 초기화
dp = [1]*n

#가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1,n):
    for j in range(i):
        if array[j] < array[i]:
            #dp[i]가 크면 과거 누적된 병수가 더 많다, dp[j]+1이 더 크다면 새로운 병사가 dp에 추가
            dp[i] = max(dp[i], dp[j]+1)

#열외시켜야 하는 병사의 수 출력
print(n - max(dp))