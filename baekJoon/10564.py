import sys

# 현재까지 한 팔굽혀펴기 횟수를 cnt, 현재 득점한 순간이 끝에서 부터 몇번째 순간인지를 turn이라고 할 때 
# 얻을 수 있는 최대 점수를 리턴하는 함수
def go(cnt, turn):
    # Base Case : 팔굽혀펴기 갯수를 정확히 충족하는 경우
    if cnt == 0:
        return 0
    # Memoization
    if dp[cnt][turn] != -1:
        return dp[cnt][turn]
    dp[cnt][turn] = -9876543210
    # 점화식
    for i in range(m):
        # 현재 점수의 기여도를 뺐을 때 0 이상이 되는 경우
        if cnt - turn * arr[i] >= 0:
            dp[cnt][turn] = max(dp[cnt][turn], go(cnt - turn * arr[i], turn + 1) + arr[i])
    return dp[cnt][turn]

# tc : 테스트케이스의 수
tc = int(sys.stdin.readline())
for _ in range(tc):
    # 입력부
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 현재까지 한 팔굽혀펴기 횟수를 cnt, 현재 득점한 순간이 끝에서 부터 몇번째 순간인지를 turn이라고 할 때 
    # 얻을 수 있는 최대 점수를 저장하는 2차원 상태 공간 배열
    dp = [[-1] * 101 for _ in range(n + 1)]
    
    # ans가 음수인 경우 팔굽혀펴기를 만족할 수 없는 경우이므로 -1 출력
    ans = go(n, 1)
    print(ans if ans > 0 else -1)

#reference
#https://peisea0830.tistory.com/131