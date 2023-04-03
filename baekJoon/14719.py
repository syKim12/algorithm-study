def solution(idx):
    global water
    if idx == w-1:
        return
    height = -1 # initialize height
    for i in range(idx+1, w):
        if arr[i] >= arr[i-1]:
            if i == idx+1: # when increasing point it next to initial point
                solution(i)
                return
            height = max(height, arr[i]) 
    height = min(height, arr[idx]) # water cannot be over a block
    for i in range(idx+1, w):
        if arr[i] < height:
            water += (height - arr[i])
        else: # check next pond
            solution(i)
            return
    return

h, w = map(int, input().split())
arr = list(map(int, input().split()))
water = 0

for i in range(w):
    if arr[i] > 0:
        solution(i)
        break

print(water)
