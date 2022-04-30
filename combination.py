
from collections import deque

"""
def do_something(comb):
    print(comb)


M = 3
some_list = [1, 2, 3, 4]
result=[]

def dfs(comb: deque, depth: int):
    if len(comb) == M:  # 종료 조건 1 : M개를 모두 선택했을 때
        #do_something(comb)  # 선택 후의 알고리즘 호출
        return comb
    elif depth == len(some_list):  # 종료 조건 2: 리스트의 마지막 까지 탐색했을 때
        return

    # 현재 depth의 값 포함 재귀 호출
    comb.append(some_list[depth])
    dfs(comb, depth + 1)

    # 현재 depth의 값 미포함 재귀 호출
    comb.pop()
    dfs(comb, depth + 1)


dfs(deque(), 0)
k = dfs(deque(), 0)
print(k)
"""
"""
def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next
k=combinations_2([1,2,3,4], 3)
print(k)
"""

"""
#https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
print(combination([1,2,3],2))
"""

#https://helloacm.com/the-combination-function-and-iterator-using-depth-first-search-algorithm/
def combinations(data, length):
    r = []
    def dfs(cur, pos):
        if len(cur) == length:
            r.append(cur)
        if pos == len(data):
            return
        if type(data) is list:
            for i in range(pos, len(data)):
                dfs(cur + [data[i]], i + 1)
        else:
            for i in range(pos, len(data)):
                dfs(cur + data[i], i + 1)
    if type(data) is list:
        dfs([], 0)
    else:
        dfs("", 0)
    return r

print(combinations([1,2,3],2))