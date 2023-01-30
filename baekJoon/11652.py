import sys

N = int(sys.stdin.readline())
d = dict()

for _ in range(N):
    n = int(sys.stdin.readline())
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1

sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(sorted_d[0][0])
