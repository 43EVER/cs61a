import doctest

def pair(a, b):
    return lambda need_first: a if need_first else b

def left(p):
    """
    >>> left(pair(5, 6))
    5
    >>> left(pair(5, 0))
    5
    >>> left(pair(0, 5))
    0
    """
    return p(True)

def right(p):
    """
    >>> right(pair(5, 6))
    6
    >>> right(pair(5, 0))
    0
    >>> right(pair(0, 5))
    5
    """
    return p(False)

def set_left(p, v):
    """
    >>> left(set_left(pair(5, 6), 1))
    1
    """
    return pair(v, right(p))

def set_right(p, v):
    """
    >>> right(set_right(pair(5, 6), 1))
    1
    """
    return pair(left(p), v)

def range_test():
    """
    >>> sum = 0
    >>> for i in range(3):
    ...     sum += i
    >>> print(sum)
    3
    """

if __name__ == "__main__":
    doctest.testmod()