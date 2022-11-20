from itertools import combinations

train_num = int(input())
train_list = [0] + list(map(int, input().split()))
train_limit = int(input())
train = 3

dp = [[0]*(train_num + 1) for _ in range(train_num + 1)]

for i in range(1, train_num + 1):
    train_flag = train_limit
    for j in range(i, train_num + 1):
        if train_flag > 0:
            dp[i][j] = dp[i][j-1] + train_list[j]
            train_flag -= 1
        else:
            dp[i][j] = dp[i][j-1]    
        
value_list = [dp[i][-1] for i in range(1, train_num + 1)]
comb_list = list(combinations(range(train_num), 3))
max_value = 0
for left, middle, right in comb_list:
    if abs(left - middle) == 1 or abs(middle - right) == 1: # 연속적인 경우
        continue
    else:
        max_value = max(max_value, value_list[left] + value_list[middle] + value_list[right])
print(max_value)
"""
d = {i: value_list[i] for i in range(train_num)}

sort_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sort_d)
continuous = -10
result = 0
final_train = set()
for key, value in sort_d.items():
    if train <= 0:
        break
    key_left, key_right = key - 1, key + 1
    if key_left not in final_train and key_right not in final_train: #불연속적인 경우
        result += value  
        train -= 1   
        final_train.add(key)
    continuous = key
print(result)
"""