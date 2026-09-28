import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    norm_types = {'l1':1, 'l2':None, 'linf':np.inf, 'frobenius':'fro'}
    try:
        ord = norm_types[norm_type]
    except ValueError:
        raise
    if norm_type == 'frobenius':
        try:
            return np.linalg.norm(arr, ord=ord)
        except ValueError:
            raise

    flatten = arr.reshape(-1)
    return np.linalg.norm(flatten, ord=ord)
    pass
