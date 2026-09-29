import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	res = {'magnitude' : 0, 'direction' : [], 'descent_direction' : []}
	res['magnitude'] = np.linalg.norm(gradient, ord=None)
	if res['magnitude'] == 0:
		res['direction'] = list(np.zeros(len(gradient)))
		res['descent_direction'] = res['direction']
		return res
	res['direction'] = gradient/res['magnitude']
	res['descent_direction'] = res['direction']*(-1.0)
	return res
	pass