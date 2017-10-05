def debt(b0, r, q):
    """(num,float,float) -> None (print num)

    b0 -> balance
    r -> annualInterestRate
    q -> monthlyPaymentRate
    r/12 -> Monthly interest rate = (Annual interest rate) / 12.0
    p -> Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    ub -> Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    b -> Updated balance each month = (Monthly unpaid balance)
         + (Monthly interest rate x Monthly unpaid balance)

    The output has a uncertainity of +/- 0.05

    >>> debt(42,0.2,0.04)
    Remaining balance: 31.38
    >>> debt(269,0.18,0.06)
    Remaining balance: 153.07
    """
    # minimum payment
    p = b0 * q
    # unpaid balance
    ub = b0 - p
    # monthly interest rate
    ir = (r/12)*ub

    for i in range(1, 13):
        # update balance each month
        b = ub + ir
        # minimum monthly payment
        p = round(b * q, 2)
        # monthly unpaid balance
        ub = b - p
        # monthly interest rate
        ir = round((r/12)*ub, 2)

    print("Remaining balance: " + str(round(b, 2)))

debt(balance, annualInterestRate, monthlyPaymentRate)
