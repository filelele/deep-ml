import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	len_func = len(functions)
	comp_list = []
	for i in range(len_func):
		func_name = functions[len_func-i-1]
		if func_name == "square":
			comp_list.append(2*x)
			x = x**2
		elif func_name == "sin":
			comp_list.append(math.cos(x))
			x = math.sin(x)
		elif func_name == "exp":
			comp_list.append(math.exp(x))
			x = math.exp(x)
		elif func_name == "log":
			comp_list.append(1/x)
			x = math.log(x)
	ret = 1
	for i in range(len(comp_list)):
		ret = ret*comp_list[i]
	return ret
	pass