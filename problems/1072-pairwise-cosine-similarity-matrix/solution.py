import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    eps=1e-4
    X = np.array(X)
    len_x = len(X)
    x_norm = np.linalg.norm(X, axis=-1, keepdims=True)+eps
    zero_norm_mask = (x_norm[:]<eps).squeeze(-1)
    ret= (X/x_norm)@(X.T/x_norm.T)

    ret[zero_norm_mask] = np.zeros(len_x)

    return ret
    pass