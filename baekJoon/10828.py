import sys

N = int(sys.stdin.readline())
q = []
for _ in range(N):
    var = sys.stdin.readline().split()
    command = var[0]
    length = len(q)
    if command == 'push':
        num = int(var[1])
        q.append(num)
    elif command == 'pop':
        if length > 0:
            print(q.pop())
        else:
            print(-1)
    elif command == 'size':
        print(length)
    elif command == 'empty':
        if length > 0:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if length == 0:
            print(-1)
        else:
            print(q[-1])