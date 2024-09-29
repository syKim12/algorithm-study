# ['####', 
# '##.#', 
# '.#.#']

from collections import deque

def check(i, j, M, N, grid):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    check_visited = [[0]*M for _ in range(N)]
    check_visited[i][j] = 1 
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                return False
            elif not check_visited[nx][ny] and grid[nx][ny] == '.':
                q.append((nx, ny))
    return True

def solution(grid):
    # '.'이 도형 안에 있는지 확인
    

    def bfs(i, j):
        dx = [0, 1, 0, -1, 1, -1, 1, -1]
        dy = [1, 0, -1, 0, 1, -1, -1, 1]
        q = deque()
        cnt = 1
        l =[(i, j)]
        q.append((i, j))
        dot_flag = 0
        between_flag = [0]*N
        dot_list = []
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        if  grid[nx][ny] == '#':
                            dot_flag = 1
                            cnt += 1
                            q.append((nx, ny))
                        else: # '.' 일 때
                            dot_list.append((nx, ny))
        for i, j in dot_list:
            if check(i, j, M, N, grid):
                cnt += 1
        """
        if len(l) > 1:
            cnt = 0
            flag = -1
            l.sort()
            print(l)
            for i in range(len(l)):
                if l[i][0] == flag:
                    cnt += l[i][1] - l[i-1][1]
                else:
                    cnt += 1
                flag = l[i][0]
            print("bfs cnt:", cnt)
            return cnt
        """    
        if not dot_flag:
            return 0
        return cnt
    
    
    answer = 0
    N, M = len(grid), len(grid[0])
    start_list = []
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                start_list.append((i, j))

    for i, j in start_list:
        if not visited[i][j]:
            #print((i, j))
            visited[i][j] = 1
            answer += bfs(i, j)
    print("answer", answer)
    return answer



solution(['####', '##.#', '.#.#'])
solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."])