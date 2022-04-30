n, m = map(int, input().split())
chicken, house = [], []

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

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = combinations(chicken, m)


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
