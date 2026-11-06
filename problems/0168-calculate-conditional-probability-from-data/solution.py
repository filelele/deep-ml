def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    eps = 1e-5
    nomin = 0
    denomin = eps

    for i in range(len(data)):
      if data[i][0] == x:
        denomin +=1
      if data[i][1] == y and data[i][0] == x:
        nomin += 1
    return nomin/denomin
    pass