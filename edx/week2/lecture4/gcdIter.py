def gcdIter(a, b):
    '''(int, int) -> int
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.

    >> gcdIter(2, 12)
    2
    >> gcdIter(9, 12)
    3
    '''
    divisor = 1
    # min number
    m = min(a,b)
    # check every number from 1 to m
    while divisor <= m:
        # is a common divisor?
        if (a%divisor==0 and b%divisor==0):
            gcd = divisor
        divisor += 1
    
    return gcd