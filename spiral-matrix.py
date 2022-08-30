rows, cols = map(int, input().split())

matrix = [[0] * cols for _ in range(rows)]

#  0,  1  right
#  1,  0  down
#  0, -1  left
# -1,  0  up
by_row, by_col = 0, 1
r, c = 0, 0

for num in range(1, rows * cols + 1):
    matrix[r][c] = num
    # change direction
    if matrix[(r + by_row) % rows][(c + by_col) % cols]:
        by_row, by_col = by_col, -by_row 
    # move by direction
    r += by_row
    c += by_col
    
[print(*[str(el).ljust(3) for el in row]) for row in matrix]
