def payBi(b0, r):
    """(num,float) -> None (print float)

    b0 -> balance
    r -> annual interest rate
    r/12 -> monthly interest rate
    ir -> interest =  (monthly interest rate) x (balance)
    ub -> Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    b -> Updated balance each month = (Monthly unpaid balance)
         + (Monthly interest rate x Monthly unpaid balance)
    low -> monthly payment lower bound = Balance / 12
    hi -> Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

    >>> payBi(320000, 0.2)
    29157.09
    >>> payBi(999999, 0.18)
    90325.03
    """
    # monthly payment lower bound
    low = b0 / 12
    # monthly payment upper bound
    hi = (b0 * (1 + (r / 12))**12) / 12
    # initial lower payment
    p = (hi + low)/2
    # payment must be in dollars with cents (multiple of 0.01)
    epsilon = 0.01

    # initial balance
    b = b0
    # unpaid balance
    ub = b - p
    # interest
    ir = (r/12)*ub

    while True:
        # check if current p will pay off the debt
        for i in range(1, 13):
            b = ub + ir
            ub = b - p
            ir = (r/12)*ub

        # if debt difference still greater than 0.01
        if round(abs(b), 2) > epsilon:
            # debt is positive?
            if b > 0:
                low = p
                p = (low + hi) / 2
            # or debt is negative?
            else:
                hi = p
                p = (low + hi)/2

            # update values for the new p
            b = b0
            ub = b - p
            ir = (r/12)*ub
        # otherwise p was found
        else:
            break

    print("Lowest payment:", round(p, 2))

payBi(balance, annualInterestRate)
