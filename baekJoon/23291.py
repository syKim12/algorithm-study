import sys
from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
stack = list(map(int, input().split()))
cnt = 0

#while max(stack) - min(stack) > K:

# 처음 어항 정리
cnt += 1
height = 1  
length = len(stack)
start = 0
temp_stack = [[0]*(length-start-1)]
temp_arr = [stack[start]]
stack = list(stack)[start+1:]
temp_stack.append(stack)
stack = deepcopy(temp_stack)
# 90도 회전 안해도됨
rotated_arr = temp_arr[:]
# 값 넣기
for i in range(len(rotated_arr)):            
    stack[0][i] = rotated_arr[i]
length = len(stack[0])
height = len(stack)
start = len(rotated_arr)-1
while height <= length - (start+1):
    stack = [stack[i][start:] for i in range(height)]    
    temp_arr = [[stack[i][j] for j in range(start)] for i in range(height)]
    if len(temp_arr[0]) + 1 > height: # 회전을 하기 위해 새로운 행 추가해야될때
        temp_stack = [[0]*(length-start-1)]
        temp_stack = temp_stack + stack
        stack = deepcopy(temp_stack)    
    print(stack)
    #90도 회전
    rotated_arr = [[temp_arr[i][j] for i in range(height-1, -1,-1)] for j in range(start)]

    # 값 넣기
    for i in range(len(rotated_arr)):
        for j in range(len(rotated_arr[0])):
            if stack[i][j] == 0:
                stack[i][j] = rotated_arr[i][j]
    height = len(stack)
    length = len(stack[0])
     # start num 찾기
    for i in range(length-1, -1, -1):
        if stack[0][i] > 0:
            start = i
            break   

    print(stack)
# break 조건?


"""
# stack 한 줄로 만들기
# stack이 이미 한줄일때 고려
row_stack = []
#if type(stack[0]) is int:
#    continue
if type(stack[0]) is list:
    for y in range(len(stack[0])):
        for x in range(len(stack)-1, -1, -1):
            if stack[x][y] > 0:
                row_stack.append(stack[x][y])
stack = row_stack[:]
    

print(cnt)
"""

