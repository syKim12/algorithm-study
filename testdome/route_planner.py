def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0]*len(map_matrix[0]) for _ in range(len(map_matrix))]
    q = [(from_row, from_column)]
    visited[from_row][from_column] = 1
    while q:
        x, y = q.pop(0)
        if x == from_row and y == from_column:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y  + dy[i]
            if 0 <= nx < len(map_matrix) and 0 <= ny < len(map_matrix[0]):
                if not visited[nx][ny] and map_matrix[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return False

if __name__ == '__main__':
    map_matrix = [
        [False, True, True],
        [True, True, False],
        [True, False, True],
        [True, True, True]
    ];

    print(route_exists(1, 0, 2, 2, map_matrix))