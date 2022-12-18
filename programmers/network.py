"""
def solution(n, computers):
    # 자기 자신에서 자기 자신은 방문 노드로 표시
    cnt = 0
    visited = [[0 ] *n for _ in range(n)]
    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y>= n:
            return False
        if not visited[x][y] and computers[x][y]:
            visited[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y)
            return True
        return False

    for i in range(n):
        for j in range(n):
            if i == j:
                visited[i][j] = 1
            if dfs(i, j) == True:
                cnt += 1

    return cnt
"""
"""

def solution(n, computers):
    # 자기 자신에서 자기 자신은 방문 노드로 표시
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y>= n:
            return False
        if x!= y and not visited[x][y] and computers[x][y]:
            visited[x][y] = 1
            visited[y][x] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x - 1, y - 1)
            dfs(x - 1, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y + 1)
            dfs(x, y + 1)
            dfs(x + 1, y)
            print(x, y, "a")
            return True
        #하나의 노드 -> 네트워크 하나 추가될 때
        if x == y and not visited[x][y]:
            print(x,y)
            visited[x][y] = 1
            for i in range(n):
                if i != x:
                    if visited[x][i]:
                        return False
                    if computers[x][i]:
                        return False
            return True
                
        return False
    
    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                print(i, j, "b")
                cnt += 1
    
    return cnt


"""

"""
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1
    return answer

def dfs(n, computers, com, visited):
    visited[com] = 1
    for connect in range(n):
        if connect != com and computers[com][connect]:
            if not visited[connect]:
                dfs(n, computers, connect, visited)
"""