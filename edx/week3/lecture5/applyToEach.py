"""
Exercise: apply to each 1

For each of the following questions 
(which you may assume is evaluated independently of the previous questions,
so that testList has the value indicated above), provide an expression
using applyToEach, so that after evaluation testList has the indicated value. 
You may need to write a simple procedure in each question to help with this process.
"""

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# must return [1, 4, 8, 9]
def absolute(item):
    """
    returns the absolute value of item
    """
    return abs(item)
applyToEach(testList, f)

# must return [2, -3, 9, -8]
def plusOne(item):
    """
    return item plus one
    """
    return item + 1
applyToEach(testList, plusOne)

# must return [1, 16, 64, 81]
def square(item):
    """
    returns the square of item
    """
    return item*item
applyToEach(testList, square)
