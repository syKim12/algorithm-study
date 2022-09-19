"""
def solution(survey, choices):
    answer = ''
    # R, C, J, A
    p1_index = ["R", "C", "J", "A"]
    p1 = [0, 0, 0, 0]
    # T, F, M, N
    p2_index = ["T", "F", "M", "N"]
    p2 = [0, 0, 0, 0]
    score = [3, 2, 1, 0, 1, 2, 3]
    # 점수 계산
    for n in range(len(survey)):
        c = choices[n]
        for i in range(4):
            if survey[n][0] == p1_index[i]:
                if c < 4:
                    p1[i] += score[c - 1]
                elif c > 4:
                    p2[i] += score[c - 1]
            elif survey[n][0] == p2_index[i]:
                if c < 4:
                    p2[i] += score[c - 1]
                elif c > 4:
                    p1[i] += score[c - 1]
    # 유형 출력
    for i in range(4):
        if p1[i] >= p2[i]:
            answer += p1_index[i]
        else:
            answer += p2_index[i]
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
"""
from collections import deque

"""
def dfs1(queue1, queue2, origin_queue1, origin_queue2):
    global cnt
    if cnt > 0 and queue1 == origin_queue1 and queue2 == origin_queue2:
        print(queue1, queue2, cnt)
        return -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if sum1 == sum2:
        return cnt
    else:
        a = queue1.popleft()
        queue2.append(a)
        cnt += 1
        return dfs2(queue1, queue2, origin_queue1, origin_queue2)


def dfs2(queue1, queue2, origin_queue1, origin_queue2):
    global cnt
    if cnt > 0 and queue1 == origin_queue1 and queue2 == origin_queue2:
        print("dfs2", queue1, queue2, cnt)
        return -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if sum1 == sum2:
        return cnt
    else:
        b = queue2.popleft()
        queue1.append(b)
        cnt += 1
        return dfs1(queue1, queue2, origin_queue1, origin_queue2)

cnt = 0
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    # 초기 값 복사
    origin_queue1, origin_queue2 = queue1.copy(), queue2.copy()
    n1 = dfs1(queue1, queue2, origin_queue1, origin_queue2)
    n2 = dfs2(queue1, queue2, origin_queue1, origin_queue2)
    print(n1, n2)
    answer = min(n1, n2)

    # answer = -2
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
"""
def bfs(queue1, queue2):
    

cnt = 0
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    return answer