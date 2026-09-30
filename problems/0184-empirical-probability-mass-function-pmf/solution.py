import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if isinstance(samples, list):
        samples = np.array(samples)
    else: 
        return -1
    
    res = []
    vals, counts = np.unique(samples, return_counts=True)
    total_counts = np.sum(counts)

    for val, count in zip(vals, counts):
        res.append((val, count/total_counts))
    return res
    pass