"""
from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    n = len(tickets) + 1
    q.append(["ICN", [], ["ICN"]])
    while q:
        start, used, path = q.popleft()
        for ticket in tickets:
            if ticket[0] == start and ticket not in used:
                temp1 = used[0:]
                temp1.append(ticket)
                temp2 = path[0:]
                temp2.append(ticket[1])
                q.append([ticket[1], temp1, temp2])
                if len(temp2) == n:
                    answer.append(temp2)
    answer.sort()
    answer = answer[0]
    return answer
"""
from collections import deque


def solution(tickets):
    answer = []
    q = deque()
    n = len(tickets)
    visited = [0] * n
    q.append(["ICN", visited, ["ICN"]])

    while q:
        start, visited, path = q.popleft()
        for i in range(n):
            # not in used를 visited list로 바꾸기
            if tickets[i][0] == start and not visited[i]:
                temp1 = visited[0:]
                temp1[i] = 1
                temp2 = path[0:]
                temp2.append(tickets[i][1])
                q.append([tickets[i][1], temp1, temp2])
                if len(temp2) == n + 1:
                    answer.append(temp2)
    answer.sort()
    answer = answer[0]
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))