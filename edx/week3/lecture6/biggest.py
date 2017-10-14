"""
Exercise: biggest

This time, write a procedure, called biggest, which returns the key corresponding to the entry
with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.

Example
>>> biggest(animals)
'd'
"""

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if (len(aDict) < 1):
        return None

    largerKey = ""
    lenKey = len(largerKey)
    for key in aDict:
        if len(aDict[key]) > lenKey:
            largerKey = key
            lenKey = len(aDict[key])
    return largerKey
