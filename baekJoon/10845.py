from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    var = sys.stdin.readline().split()
    command = var[0]
    length = len(q)
    if command == 'push':
        q.append(int(var[1]))
    elif command == 'pop':
        if length == 0:
            print(-1)
        else:
            temp_pop = q.popleft()
            print(temp_pop)
    elif command == 'size':
        print(length)
    elif command == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if length == 0:
            print(-1)
        else:
            print(q[0])
    elif command == 'back':
        if length == 0:
            print(-1)
        else:
            print(q[-1])
    