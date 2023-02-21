import sys
from heapq import heappop, heappush

def debug(ls):
    for l in ls:
        print(l)
    return

# test case example
# 3 3 2
# 1 2 3
# 1 3 1
# answer: 1

city, limit, route = map(int, sys.stdin.readline().split())
arr = [[1e9*(-1)]*(city+1) for _ in range(city+1)] 
dp = [[1e9*(-1)]*(limit+1) for _ in range(city+1)] # 실제로 갈 수 없는데 arr[prev_city][now_city] 값이 양수여서 값이 계산되는 경우 방지

for _ in range(route):
    i, j, meal = map(int, sys.stdin.readline().split())
    arr[i][j] = max(arr[i][j], meal)

dp[1][1] = 0 # 위에서 전부 -1e9 으로 값을 뒀기 때문에 첫 시작 값은 0으로
for lmt in range(2, limit+1): # limit이 1인 경우는 1번 도시만 가능하므로 2부터 시작
    for now in range(2, city+1): # 첫번째 도시에서 limit이 2 이상인 경우는 없으므로 2부터 시작
        for prev in range(1, now): # e.g. 3번 도시로 가는 경우는 1 -> 3, 2 -> 3이 있다.
            # 이전 도시에서 한번 이동할 때는 움직인 값에서 무조건 +1이 되므로 dp[prev][lmt-1]+arr[prev][now], 
            # 도시에서 도시로 이동이 불가능한 경우는 arr값이 -1e9이므로 조건을 나누지 않는다.
            dp[now][lmt] = max(dp[now][lmt], dp[prev][lmt-1]+arr[prev][now])
print(max(dp[-1]))
        