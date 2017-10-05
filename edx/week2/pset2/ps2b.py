def minFix(b0, r):
    """(num,float) -> None (print int)

    b0 -> balance
    r -> annual interest rate
    r/12 -> monthly interest rate
    ir -> interest =  (monthly interest rate) x (balance)
    ub -> Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    b -> Updated balance each month = (Monthly unpaid balance)
         + (Monthly interest rate x Monthly unpaid balance)

    >>> minFix(3329, 0.2)
    310
    >>> minFix(4773, 0.2)
    440
    """

    # initial lowest monthly payment
    p = 10
    # unpaid balance
    ub = b0 - p
    # interest
    ir = (r/12)*ub

    while True:
        # check if p will pay off debt in under one year
        for i in range(1, 13):
            # update balance each month
            b = ub + ir
            # monthly unpain balance
            ub = b - p
            # monthly interest rate
            ir = round((r / 12)*ub, 2)

        # current p pays off the debt in under one year
        if b <= 0:
            break

        # check for the next p and update values for the that p
        else:
            p += 10
            ub = b0 - p
            ir = (r/12)*ub

    print("Lowest payment:", p)

minFix(balance, annualInterestRate)
