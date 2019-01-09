"""
There are many ways to Fibonacci.
This module contains a few solutions with varying approaches,
some essentially the same,
but not all of them have the same input / output.

Note that `fibonacci_recurse` is significantly slower than `fibonacci_memoized`,
with the only change being the added memoization
TODO create a benchmark
"""


def fibonacci_recurse(num):
    """
    :param int num: a place / "slot" in the Fibonacci Sequence,
        must be greater than or equal to zero.
    :return: the number found at a specific place in the Fibonacci Sequence
    :rtype: int
    :raises RecursionError: recursion may go too deep
    """
    # NOTE using name "num" instead of "n" since "n" is used for "next" in debugger
    if num in (0, 1):
        return num
    return fibonacci_recurse(num-1) + fibonacci_recurse(num-2)


def _fibonacci_memoized_recurse(num, memo):
    """
    overlapping subtrees make the recursive solution a candidate for memoization
    """
    try:
        # at first this just contains the base cases,
        # values get filled in as needed
        result = memo[num]
    except IndexError:
        result = _fibonacci_memoized_recurse(num-1, memo) + _fibonacci_memoized_recurse(num-2, memo)
        # due to order of calls,
        # we can append knowing the fib number goes to the correct index
        # alternative approach is extending the memo with `None`s and assigning in the result by index
        memo.append(result)
    return result


def fibonacci_memoized(num):
    """
    Use memoization so we don't have to repeat the same calls between overlapping subtrees
    in the recursive callstack.

    Example, we see repeated fib calls to the same number:

                            fib(5)
                 fib(4)                           fib(3)
           fib(3)        fib(2)              fib(2)    fib(1)
        fib(2)  fib(1)  fib(1) fib(0)     fib(1) fib(0)
    fib(1) fib(0)
    """
    memo = [0, 1]  # base cases start in memo, we no longer require the `if` statements
    return _fibonacci_memoized_recurse(num, memo)


def fibonacci_bottom_up(num):
    """
    :param num int: position in the Fibonacci Sequence
    :return: value of position `num` in the Fibonacci Sequence
    """
    # bottom-up approach
    # based on CS Dojo's video: https://youtu.be/vYquumk4nWw?t=736
    # also essentially the same as: https://youtu.be/e0CAbRVYAWg?t=202

    if num in (0, 1):
        # still need to return base cases manually,
        # they don't work with the strategy below.
        # e.g. `num` of 0 is incompatible with the index access below
        return num

    # populate list to desired length so we can assign without getting IndexError
    # +1 item for the zero index
    # bottom_up[num] to be the num-th number in the sequence
    bottom_up = [None] * (num+1)
    bottom_up[0] = 0
    bottom_up[1] = 1
    # populate the list with the actual values,
    # where i-th number in the series is at index i in the list
    for i in range(2, num+1):  # +1 so we include our target number
        # add previous two values to get next in the sequence, as per usual fib
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[num]


def fibonacci_upto_num_dp(target):
    """
    Create list containing Fibonacci Sequence up to `target`,
    starting from 0 until a positive integer is reached greater than target.
    Reaches a value as opposed to a position in the series.
    :param int num: The value to reach in the sequence,
        including that number if in the sequence.
    :return: list of Fibonacci Sequence numbers less than or equal to target
    :rtype: list
    """
    sequence = []
    a, b = 0, 1
    while a <= target:
        sequence.append(a)
        a, b = b, a+b
    else:
        return sequence
