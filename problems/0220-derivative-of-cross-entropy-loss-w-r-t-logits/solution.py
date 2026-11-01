def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	import numpy as np
	softmax = lambda x: np.e**(x-np.max(x))/np.sum(np.e**(x-np.max(x)))
	onehot_encode = lambda len_x, target: np.eye(len_x)[target]
	cross_entropy_loss = lambda x, y_target: np.sum((-np.log(softmax(x)))*onehot_encode(len(x), y_target))

	ret = []
	eps = 1e-5
	logits_orig = np.array(logits)
	for i in range(len(logits)):
		diff = np.zeros(len(logits_orig))
		diff[i] = eps
		ret.append((cross_entropy_loss(logits_orig + diff, target) - cross_entropy_loss(logits_orig, target))/eps)
	return ret
	pass