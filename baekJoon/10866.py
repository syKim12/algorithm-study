from collections import deque
import sys 
N = int(sys.stdin.readline())

q = deque()
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        q.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        q.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif command[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])