def evalQuadratic(a, b, c, x):
    '''(num, num, num, num) -> num
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    This function evaluates a quadratic equation.

    >>  evalQuadratic(1,2,3,4)
    27
    >> evalQuadratic(1,2,-24,4)
    0
    '''
    return a*x**2 + b*x + c