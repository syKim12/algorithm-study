import sys

lecture, bluray = map(int, sys.stdin.readline().split())
lecture_list = list(map(int, sys.stdin.readline().split()))

start, end = lecture_list[0], lecture_list[-1]
while start <= end:
    size = (start + end) // 2
    lecture_sum, cnt = 0, 0
    for i in range(lecture):
        lecture_sum += lecture_list[i]
        if lecture_sum > size:
            lecture_sum = 0
            cnt += 1
    if cnt >= bluray:
        start = size+1
    else:
        end = size-1

