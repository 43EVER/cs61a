import doctest


import doctest

def remove_digit(n, digit):
    """
    >>> remove_digit(999, 9)
    0
    >>> remove_digit(1231, 1)
    23
    """
    if n == 0:
        return 0
    if n % 10 == digit:
        return remove_digit(n // 10, digit)
    return remove_digit(n // 10, digit) * 10 + n % 10

def num_digits(n):
    if n < 10:
        return 1
    return 1 + num_digits(n // 10)

def reverse_digits(n):
    """
    >>> reverse_digits(123)
    321
    >>> reverse_digits(0)
    0
    >>> reverse_digits(123000)
    321
    >>> reverse_digits(102)
    201
    """
    if n < 10:
        return n
    
    return (n % 10) * (10 ** (num_digits(n) - 1)) + reverse_digits(n // 10)

def interleave_digits(a, b):
    """
    >>> interleave_digits(123, 456)
    142536
    >>> interleave_digits(0, 9)
    9
    >>> interleave_digits(10000000000, 99999999999)
    1909090909090909090909
    """
    if a < 10:
        return a * 10 + b
    return interleave_digits(a // 10, b // 10) * 100 + interleave_digits(a % 10, b % 10)

def pair(a, b):
    return 2**a * 3**b

def multiplicity(factor, n):
    if n % factor == 0:
        return 1 + multiplicity(factor, n / factor)
    return 0

def left(p):
    """
    >>> left(pair(5, 6))
    5
    >>> left(pair(5, 0))
    5
    >>> left(pair(0, 5))
    0
    """
    return multiplicity(2, p)

def right(p):
    """
    >>> right(pair(5, 6))
    6
    >>> right(pair(5, 0))
    0
    >>> right(pair(0, 5))
    5
    """
    return multiplicity(3, p)

if __name__ == "__main__":
    doctest.testmod()