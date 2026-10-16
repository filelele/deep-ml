import numpy as np
import math

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	x = point[0]
	y = point[1]
	if len(point) == 3:
		z = point[2]
	if func_name == "poly2d":
		df_dx = 2*y*x + y**2
		df_dy = x**2 + 2*x*y
	elif func_name == "exp_sum":
		df_dx = math.exp(x+y)
		df_dy = df_dx
	elif func_name == "product_sin":
		df_dx = math.sin(y)
		df_dy = x*math.cos(y)
	elif func_name == "poly3d":
		df_dx = 2*y*x
		df_dy = x**2 + z**2
		df_dz = 2*y*z
	elif func_name == "squared_error":
		df_dx = 2*(x-y)
		df_dy = -2*(x-y)
	if len(point) == 3:
		return (df_dx, df_dy, df_dz)
	else:
		return (df_dx, df_dy)
	pass