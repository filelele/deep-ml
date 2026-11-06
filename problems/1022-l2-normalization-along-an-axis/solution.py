import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    # Your code here
    eps = 1e-5
    l2_norm = np.linalg.norm(x, axis=axis, keepdims=True) + eps
    return x/l2_norm
    pass
