"""
Explanation:

sum([2, 4, 6, 10]) ->
2 + sum([4, 6 ,10])

sum([4, 6 ,10]) ->
4 + sum([6, 10])

sum([6, 10]) ->
6 + sum([10])  <- base case
"""


def recursive_sum(lst, num=0):
    """
    Sum a list of integers using recursion.
    This serves as a simple example of a recursive function.

    :param lst list: List of integers to add together.
        Only necessary top level argument.
    :param num int: Number added to sum of everything else.
        Starts as neutral element, zero.
    """
    if not lst:
        # base case
        # when a single item list is passed,
        # it is processed into a `num` arg and an empty list
        return num
    return num + recursive_sum(lst[1:], num=lst[0])
