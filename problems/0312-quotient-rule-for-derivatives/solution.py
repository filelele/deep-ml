import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    try:
        max_g_exponent = len(g_coeffs) - 1
        max_h_exponent = len(h_coeffs) - 1
        
        h_x = []
        for i in range(len(h_coeffs)):
            expo = max_h_exponent - i
            c = h_coeffs[i]
            h_x.append(c*(x**expo))
        h_x = sum(h_x)

        g_x = []
        for i in range(len(g_coeffs)):
            expo = max_g_exponent - i
            c = g_coeffs[i]
            g_x.append(c*(x**expo))
        g_x = sum(g_x)
        
        dg_dx = []
        for i in range(len(g_coeffs)):
            c = g_coeffs[i]*(max_g_exponent - i)
            expo = max_g_exponent - i - 1
            dg_dx.append(c*(x**expo))
        dg_dx = sum(dg_dx)

        dh_dx = []
        for i in range(len(h_coeffs)):
            c = h_coeffs[i]*(max_h_exponent - i)
            expo = max_h_exponent - i - 1
            dh_dx.append(c*(x**expo))
        dh_dx = sum(dh_dx)
        
        return (dg_dx*h_x - dh_dx*g_x)/(h_x**2)
    except ZeroDivisionError:
        return -1.0
    pass