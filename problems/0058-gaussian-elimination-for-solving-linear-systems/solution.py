import numpy as np

def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	tol = 1e-6
	b = np.expand_dims(b, axis=1)
	A = np.concatenate([A,b], axis=1)

	for row,col in zip(range(A.shape[0]-1), range(A.shape[1])):
		k = row
		while k < A.shape[0] and np.abs(A[k, col]) < tol:
			k = k+1
		if k == A.shape[0] - 1:
			continue
		eli_row = A[k].copy()
		A[k] = A[row]
		A[row] = eli_row

		for subrow in range(row + 1, A.shape[0]):
			m = A[row]*(-1)*(A[subrow,col]/A[row,col])
			A[subrow] = A[subrow].astype(float).copy() + m

	x = np.zeros(A.shape[0])
	for i in range(A.shape[0]):
		 x[len(x) - 1 - i] = (A[len(x) - 1 - i, -1] -  A[len(x) - 1 - i, :-1]@x)/A[len(x) - 1 - i, len(x) - i - 1]


	return x
