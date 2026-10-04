import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	num_samples = len(vectors[0])

	mat = np.array(vectors)
	mat = mat - np.mean(mat, axis=1, keepdims=True)

	return (mat@mat.T)/(num_samples-1)