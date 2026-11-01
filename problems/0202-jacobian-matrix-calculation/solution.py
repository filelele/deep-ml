import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	ret = []
	len_x = len(x)
	f_orig = np.array(f(x))
	x_orig = np.array(x)

	for i in range(len_x):
		diff = np.zeros(len_x)
		diff[i] = h
		x_i = x + diff
		f_i = np.array(f(x_i.tolist()))
		ret.append((f_i - f_orig)/h)
	ret = np.array(ret)
	ret = ret.T
	return ret.tolist()
	pass