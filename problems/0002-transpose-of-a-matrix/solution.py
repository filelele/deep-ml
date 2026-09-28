def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row = len(a)
    col = len(a[0])
    a_T = []
    for i in range(col):
        row_i = []
        for j in range(row):
            row_i.append(a[j][i])
        a_T.append(row_i)
    return a_T    
    pass