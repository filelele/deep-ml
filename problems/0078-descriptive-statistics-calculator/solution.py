import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    if not isinstance(data, (list, np.ndarray)):
        return -1
    if isinstance(data, list):
        data = np.array(data)
    flatten_data = data.ravel()
    res = {}
    res['mean'] = flatten_data.mean()
    res['median'] = np.median(flatten_data)
    vals, counts = np.unique(flatten_data, return_counts=True)
    res['mode'] = vals[np.argmax(counts)]
    res['variance'] = np.var(flatten_data, ddof=0)
    res['standard_deviation'] = np.sqrt(res['variance'])
    res['25th_percentile'], res['50th_percentile'], res['75th_percentile'] = np.percentile(flatten_data, [25,50,75])
    res['interquartile_range'] = res['75th_percentile'] - res['25th_percentile']
    return res
    pass