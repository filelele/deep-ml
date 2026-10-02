import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	trace = 0
	for i in range(len(matrix)):
		trace += matrix[i][i]
	det = np.linalg.det(np.array(matrix))
	return (float(det), trace)
	pass