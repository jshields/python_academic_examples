

def fibonacci_recurse(num):
    """
    :param int num: a place / "slot" in the Fibonacci Sequence,
        must be greater than or equal to zero.
    :return: the number found at a specific place in the Fibonacci Sequence
    :rtype: int
    :raises RecursionError: recursion may go too deep
    """
    # NOTE using name "num" instead of "n" since "n" is used for "next" in debugger
    if num == 0:
        return 0
    if num == 1:
        return 1
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



def fibonacci_dp(num):
    # TODO
    pass


def fibonacci_upto_num_dp(num):
    """
    Create list containing Fibonacci Sequence up to `num` n,
    starting from 0 until a positive integer is reached greater than n.
    :param int num: The value to reach in the sequence,
        including that number if in the sequence.
    :return: list of Fibonacci Sequence numbers less than or equal to ns
    :rtype: list
    """
    sequence = []
    a, b = 0, 1
    while a <= num:
        sequence.append(a)
        a, b = b, a+b
    else:
        return sequence
