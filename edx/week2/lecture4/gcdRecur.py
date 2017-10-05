def gcdRecur(a, b):
    '''(int, int) -> int
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.

    >> gcdIter(2, 12)
    2
    >> gcdIter(9, 12)
    3
    '''
    # base case
    if b == 0:
        return a
    # recursive call
    else:
        return gcdRecur(b, a % b)
