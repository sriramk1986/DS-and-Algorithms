def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    columns = []

    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 0:
                rows.append(a)
                columns.append(b)

    for row in rows:
        nullify_row(row, matrix)

    for column in columns:
        nullify_column(column, matrix)

    return matrix


def nullify_row(row, matrix):
    for i in range(0, len(matrix[0])):
        matrix[row][i] = 0


def nullify_column(column, matrix):
    for i in range(0, len(matrix)):
        matrix[i][column] = 0


matrix = ([0, 2, 3], [4, 0, 6], [7, 8, 9])
print(zero_matrix(matrix))


# Takeaway:
# if setting row or column to zero then the exact value of the zero value cell doesn't matter
