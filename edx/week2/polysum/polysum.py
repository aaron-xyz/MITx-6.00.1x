def perimeter(n, s):
    """(int,num) -> float
    This function returns the perimeter of
    a regular polygon

    perimeter = n*s

    >> perimeter(2, 45)
    90
    >> perimeter(97, 59)
    5723
    """
    return n * s


def area(n, s):
    """(int,num) -> float
    This fnction return the area of
    a regular polygon

    area of the polygon = (0.25*n*s^2)/tan(pi/n)
    where pi = 3.14159...

    >> area(2, 45)
    6.199774420683475e-14
    >> area(97, 59)
    2605467.972645256
    """
    from math import tan, pi
    area = (0.25 * n * s**2) / tan(pi/n)
    return area


def polysum(n, s):
    """(int,num)-> float
    polysum(n,s)
    A regular polygon has n number of sides. Each side has length s.
    n - introduce the number of sides of the regular polygon
    s - introduce the length of the sides

    This function return the sum of the area and
    the square of the perimeter rounded to 4 digits
    return = area +  perimeter^2

    >> polysum(2, 45)
    8100.0
    >> polysum(1, 77)
    -1.2103489765636911e+19
    >> polysum(97, 59)
    35358196.9726
    """
    return round(perimeter(n,s)**2 + area(n,s), 4)
