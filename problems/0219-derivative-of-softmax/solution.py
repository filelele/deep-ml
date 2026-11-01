def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	import numpy as np
	x_orig = np.array(x)
	softmax = lambda x: np.e**(x - np.max(x))/np.sum(np.e**(x - np.max(x)))
	
	eps = 1e-5
	ret = []
	for i in range(len(x_orig)):
		diff = np.zeros(len(x_orig))
		diff[i] += eps 
		ret.append((softmax(x+diff) - softmax(x))/eps)
	ret = np.array(ret)
	ret = ret.T
	return ret.tolist()
	pass