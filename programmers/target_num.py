from itertools import combinations
#시간 초과
"""
def solution(numbers, target):
    answer = 0
    cnt = 0
    l = ["+", "-"]*len(numbers)
    nlist = list(combinations(l, len(numbers)))
    #중복 제거 위해 set 이용
    nlist = set(nlist)
    num = 0
    for comb in nlist:
        for i in range(len(comb)):
            if comb[i] == "+":
                num += numbers[i]
                print(num)
            elif comb[i] == "-":
                num -= numbers[i]
                print(num)
        if num == target:
            cnt += 1
        print(num, cnt)
        num = 0
    answer = cnt
    return answer
print(solution([1, 1, 1, 1, 1], 3))
"""

def dfs(i, numbers, target, value):
    global cnt
    if value == target and i == len(numbers):
        cnt += 1
        return
    if i == len(numbers):
        return
    dfs(i+1, numbers, target, value + numbers[i])
    dfs(i+1, numbers, target, value - numbers[i])

cnt = 0
def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return cnt

print(solution([1, 1, 1, 1, 1], 3))