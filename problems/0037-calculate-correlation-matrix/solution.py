import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	if Y is None:
		Y = X
	X_mean = np.mean(X, axis=0)
	X = X - X_mean
	X_norm = np.linalg.norm(X, axis=0)
	X = X/X_norm
	
	Y_mean = np.mean(Y, axis=0)
	Y = Y - Y_mean
	Y_norm = np.linalg.norm(Y, axis=0)
	Y = Y/Y_norm
	return (Y.T@X).T