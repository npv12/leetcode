def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows_which_changed = []
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            rows_which_changed.extend([index for index, element in enumerate(matrix[i]) if element == 0])
            matrix[i] = [0] * len(matrix[i])
    
    for index in rows_which_changed:
        for i in range(len(matrix)):
            matrix[i][index] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)