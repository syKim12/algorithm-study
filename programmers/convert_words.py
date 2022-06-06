from collections import deque


# 한개의 알파벳만 바꿀 수 있는지 체크
def check(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
            if cnt > 1:
                return False
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    q = deque()
    q.append([begin, [], 0])
    visited = [0] * len(words)
    # bfs
    while q:
        now, l, cnt = q.popleft()

        for i in range(len(words)):
            if check(now, words[i]) and not visited[i]:
                l.append(words[i])
                visited[i] = 1
        print(now, l, cnt)
        if target == now:
            answer = cnt
            break
        else:
            for k in l:
                q.append([k, [], cnt + 1])

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))