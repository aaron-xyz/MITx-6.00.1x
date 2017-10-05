def recurPower(base, exp):
    '''(num, int) -> num
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp

    >> recurPower(2, 5)
    32
    >> recurPower(5, 3)
    125
    '''
    # Base case
    if exp <= 0:
        return 1
    # Recursive call - exp times
    else:
        return base * recurPower(base, exp-1)