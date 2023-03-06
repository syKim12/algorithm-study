import sys

amount = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))

start = 0
end = amount - 1
prev_liquid = abs(liquid[start]+liquid[end])
answer_left, answer_right = start, end
while start < end:
    now = liquid[start] + liquid[end]
    if abs(now) < prev_liquid:
        answer_left, answer_right = start, end
        prev_liquid = abs(now)
        if now == 0:
            break

    if now < 0:
        start += 1
    else:
        end -= 1
print(liquid[answer_left], liquid[answer_right])