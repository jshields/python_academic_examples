
def fibonacci_recurse(n):
    """
    :param int n: a place / "slot" in the Fibonacci Sequence,
        must be greater than or equal to zero.
    :return: the number found at a specific place in the Fibonacci Sequence
    :rtype: int
    :raises RecursionError: recursion may go too deep
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recurse(n-1) + fibonacci_recurse(n-2)


def fibonacci_print(n):
    """
    Print the Fibonacci Sequence,
    starting from 0 until a positive integer `n` is reached.
    :param int n: The value to reach in the sequence,
        including that number if in the sequence.
    """
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a+b
    else:
        print(sequence)
