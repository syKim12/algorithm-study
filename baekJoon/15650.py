from itertools import combinations

N, M = map(int, input().split())
n_list = [i for i in range(1, N+1)]
visited = [0]*(N+1)

"""
# combinations
comb_list = list(combinations(n_list, M))

for l in comb_list:
    for num in l:
        print(num, end=' ')
    print("\n", end='')
"""

# 재귀
def combination(arr, visited, idx, depth, n, r): # nCr
    # 탈출 조건
    if depth == r: # OR if len(arr) == r:
        print(arr)
        return
    # 반복 
    for i in range(idx, n+1):
        if not visited[i]:
            visited[i] = 1
            arr.append(i)
            combination(arr, visited, i + 1, depth+1, n, r)
            visited[i] = 0
            arr.pop()

combination([], visited, 1, 0, N, M)