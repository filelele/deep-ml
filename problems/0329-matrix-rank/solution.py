import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-4) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    if len(A.shape) == 1:
        ret = 0 if np.abs(A) == 0 else 1
        return ret
     
    for row,col in zip(range(A.shape[0]), range(A.shape[1])):
    # swap row without zero to first
        k = row
        while k < A.shape[0] and A[k,col] == 0:
            k+=1
        if k == A.shape[0]:
            continue

        #swap the first non-zero-at-col row to current row as compensating row
        temp = A[k].copy()
        A[k] = A[row]
        A[row] = temp

        for sub_row in range(row+1, A.shape[0]):
            A[sub_row] = A[sub_row].astype(float).copy() + (-1*(A[sub_row, col]/A[row,col]))*A[row]

    ret = 0
    for row in range(A.shape[0]):
        if np.linalg.norm(A[row], ord=None) > tol:
            ret += 1
    return ret

    pass