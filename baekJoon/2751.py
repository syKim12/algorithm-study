import sys

N = int(sys.stdin.readline())
l = []

for _ in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in range(N):
    print(l[i])