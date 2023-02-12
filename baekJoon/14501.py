days = int(input())
time = [0] * days
price = [0] * days
dp = [0] * (days+1)
max_income = 0

for day in range(days):
    t, p = map(int, input().split())
    time[day], price[day] = t, p

for i in range(days-1, -1, -1):
    if time[i] + i > days:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+time[i]]+price[i])
print(dp[0])


"""
for day in range(days):
    t, p = map(int, input().split())
    time[day], price[day] = t, p
visited = [0] * days
income_list = []
def dfs(path, idx, income):
    global max_income
    if idx >= days and idx-time[path[-1]] < days:
        #print("-------")
        print(path, income)
        #print("-------")
        if path[-1] == days-1:
            max_income = max(max_income, income-price[-1])
        else:
            max_income = max(max_income, income)
        return
    
    #elif idx == days-1:
    #    print(path, '-1')
    #    if time[idx] == 1:
    #        max_income = max(max_income, income+price[-1])
    #    else:
    #        max_income = max(max_income, income)
    #    return
    
    #print(path, idx)
    for i in range(idx, days):
        if not visited[i]:
            if len(path) > 0 and idx <= path[0]:
                continue
            visited[i] = 1
            path.append(i)
            dfs(path, idx + time[i], income + price[i])
            visited[i] = 0
            path.pop()

dfs([], 0, 0)
print(max_income)

"""
