def iterPower(base, exp):
    '''(num, int) -> num
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp

    >> recurPower(2, 5)
    32
    >> recurPower(5, 3)
    125
    '''
    result = 1
    # Multiply exp times
    for n in range(exp):
        result = result * base
    # return base^exp
    return result