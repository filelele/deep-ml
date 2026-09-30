import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	mat_np = np.array(matrix)
	res = None
	if mode == 'row':
		res = np.mean(mat_np, axis=1)
	elif mode == 'column':
		res = np.mean(mat_np, axis=0)
	return list(res.flatten())
	pass