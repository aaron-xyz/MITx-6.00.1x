"""
Exercise: how many

First, write a procedure, called how_many, which returns the sum of
the number of values associated with a dictionary. For example:

>>> print(how_many(animals))
6
"""

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for key in aDict:
        counter += len(aDict[key])
    return counter