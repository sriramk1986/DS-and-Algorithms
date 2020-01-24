def rotate_matrix(matrix):
    len_matrix = len(matrix)
    for i in range(len_matrix):
        for j in range(i, len_matrix):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len_matrix):
        left_idx = 0
        right_idx = len_matrix - 1

        while left_idx < right_idx:
            matrix[i][left_idx], matrix[i][right_idx] = (
                matrix[i][right_idx],
                matrix[i][left_idx],
            )
            left_idx += 1
            right_idx -= 1

    return matrix


def rotate_matrix_2(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        
        for i in range(first, last):
            #Top
            top = matrix[first][i]
            
            #Top takes value of left
            matrix[first][i] = matrix[last - i][first]
            
            #Left takes value of bottom
            matrix[last - i][first] = matrix[last][last - i]
            
            #Bottom takes value of right
            matrix[last][last - i] = matrix[first + i][last]
            
            #Right takes value of top
            matrix[first + i][last] = top
            
    return matrix





matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

print(rotate_matrix(matrix))
