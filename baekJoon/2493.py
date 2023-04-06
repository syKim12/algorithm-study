N = int(input())
arr = list(map(int, input().split()))
answer = [0]*N

idx, stack = [0], [arr[0]]
for i in range(1, N):
    if arr[i] < stack[-1]:
        answer[i] = idx[-1]
    else:
        idx.pop()
        stack.pop()
        idx.append(i)
        stack.append(arr[i])

"""
for i in range(1, N):
    for j in range(i-1, -1, -1):
        print(i, j)
        if arr[j] >= arr[i]:
            answer[i] = j + 1
            break
"""    
    
print(*answer)