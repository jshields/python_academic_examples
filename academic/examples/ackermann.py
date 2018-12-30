

def ackermann(m, n):
    """
    see https://en.wikipedia.org/wiki/Ackermann_function

    :type m: int
    :type n: int
    :return: Ackermann answer for (m ,n)
    :rtype: int
    :raises RecursionError: recursion will most likely go too deep
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
