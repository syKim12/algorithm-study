import sys

N = int(sys.stdin.readline())
l = [0]*10001
# get data
for _ in range(N):
    l[int(sys.stdin.readline())] += 1

# print answer
for idx in range(10001):
    temp = l[idx]
    if temp > 0:
        for _ in range(temp):
            print(idx)


"""
# 메모리 초과
# counting sort by using cnt list
cnt = [0]*(max(l) + 1)
answer = [0]*N
for num in l:
    cnt[num] += 1
for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]
for num in l:
    idx = cnt[num]
    answer[idx-1] = num
    cnt[num] -= 1
# print answer
for num in answer:
    print(num)

"""

