def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    if from_row < 0 or from_row >= len(game_matrix) or from_column < 0 or from_column >= len(game_matrix[0]) or to_row < 0 or to_row >= len(game_matrix) or to_column < 0 or to_column >= len(game_matrix[0]):
        return False
    if not game_matrix[from_row][from_column] or not game_matrix[to_row][to_column]:
        return False
    visited = [[0]*len(game_matrix[0]) for _ in range(len(game_matrix))]
    q = []
    q.append((from_row, from_column))
    visited[from_row][from_column] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.pop(0)
        if x == to_row and y == to_column:
            return True
        #print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if dy[i] == 0:
                if nx < 0 or nx >= len(game_matrix) or ny < 0 or ny >= len(game_matrix[0]) or visited[nx][ny] or not game_matrix[nx][ny]:
                    continue
                else:
                    nx += dx[i]
                    #print(nx)
               
            if nx < 0 or nx >= len(game_matrix) or ny < 0 or ny >= len(game_matrix[0]):
                continue
            elif visited[nx][ny]:
                continue
            elif not game_matrix[nx][ny]:
                continue
            #elif nx == to_row and ny == to_column:
                #print(nx, ny)
            #    return True
            else:
                visited[nx][ny] = 1
                q.append((nx, ny))
                
    return False

if __name__ == "__main__":
    game_matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    #print(can_travel_to(game_matrix, 2, 2, 0, 2))
    #print(can_travel_to(game_matrix, 2, 2, 2, 1))
    #print(can_travel_to(game_matrix, 2, 2, 2, 3))
    #print(can_travel_to(game_matrix, 2, 2, 4, 2))
    print(can_travel_to(game_matrix, 3, 3, 4, 4))