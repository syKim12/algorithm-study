import sys

n, height = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()

start = 0
end = tree[-1]

while start <= end:
    mid = (start + end)//2
    temp_sum = 0
    for t in tree:
        if t > mid:
            temp_sum += (t-mid)
        if temp_sum > height:
            break
    if temp_sum == height:
        answer = mid
        break
    elif temp_sum < height:
        end = mid - 1
    else:
        start = mid + 1

print(mid)