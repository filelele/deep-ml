import numpy as np

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	vals = np.linspace(1,n,n)
	mean = np.mean(vals)
	var = np.sum((vals - mean)**2)/n
	return (mean, var)
	pass