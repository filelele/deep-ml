def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	import math
	# Your code here
	relu_diff = lambda x: 1 if x>0 else 0
	sigmoid = lambda x: 1/(1+math.exp(-x))
	sigmoid_diff = lambda x: sigmoid(x)*(1-sigmoid(x))
	tanh_diff = lambda x: 1 - (math.tanh(x))**2
	return {'sigmoid': sigmoid_diff(x), 'tanh': tanh_diff(x), 'relu': relu_diff(x)}
	pass