import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    numerical_grad = []
    I = np.eye(len(x))
    for i in range(len(x)):
        f_left = f(x-epsilon*I[i])
        f_right = f(x+epsilon*I[i])
        numerical_grad.append((f_right - f_left)/(2*epsilon))
    numerical_grad = np.array(numerical_grad)
    rel_error = lambda x, y: np.linalg.norm(x-y)/(np.linalg.norm(x)+np.linalg.norm(y))
    rel_err = rel_error(numerical_grad, analytical_grad)
    return numerical_grad, rel_err
    pass