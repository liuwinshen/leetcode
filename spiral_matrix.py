def spiral_order(matrix):
    if len(matrix) == 0:
        return []

    spiral = []
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    column = 0

    while (row < m and column < n):
        # traverse row left to right
        for i in range(column, n):
            spiral.append(matrix[row][i])
        row += 1

        # traverse column top to bottom
        for i in range(row, m):
            spiral.append(matrix[i][n-1])
        n -= 1

        # traverse row right to left
        if (row < m):
            for i in range(n-1, column-1, -1):
                spiral.append(matrix[m-1][i])
            m -= 1

        if (column < n):
            # traverse column bottom to top
            for i in range(m-1, row-1, -1):
                spiral.append(matrix[i][column])
            column += 1

    return spiral

print(spiral_order([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],
                    [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],
                    [41,42,43,44,45,46,47,48,49,50]]))
