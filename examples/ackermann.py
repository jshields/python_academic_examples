"""
https://en.wikipedia.org/wiki/Ackermann_function
"""

def ackermann(m, n):
    """
    :param m: int
    :param n: int
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
