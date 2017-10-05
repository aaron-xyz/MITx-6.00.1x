def isIn(char, aStr):
    '''(char,string) -> boolean

    returns: True if char is in aStr; False otherwise
    char: a single character
    aStr: an alphabetized string

    >> isIn('a', '')
    False
    >> isIn('h', 'lnnnx')
    False
    >> isIn('d', 'bdgggilmmorrtuzz')
    True
    >> isIn('j', 'cjw')
    True
    '''
    # get the size of the string
    size = len(aStr)
    # midpoint
    mid = size//2
    # there's no string
    if size == 0:
        return False
    # string of only a char
    elif size == 1:
        return aStr == char
    # mid value is char
    elif aStr[mid] == char:
        return True
    # recursive call - neglect the left half
    elif aStr[mid] < char:
        return isIn(char,aStr[mid+1:])
    # recursive call - neglect the right half
    else:
        return isIn(char,aStr[:mid])