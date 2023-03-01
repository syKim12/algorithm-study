import sys

lecture, bluray = map(int, sys.stdin.readline().split())
lecture_list = list(map(int, sys.stdin.readline().split()))

start, end = max(lecture_list), sum(lecture_list)
while start <= end:
    size = (start + end) // 2
    lecture_sum, cnt = 0, 0
    for i in range(lecture):
        if lecture_sum + lecture_list[i] > size:
            lecture_sum = 0
            cnt += 1
        lecture_sum += lecture_list[i]
    if cnt >= bluray:
        start = size + 1
    else:
        end = size - 1

print(start)

