import logging

logging.basicConfig(filename='selection_sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


def selection_sort(lst):
    """
    TODO see if this works
    selection sort is a naive sorting algorithm
    Complexity:
    n + n-1 + n-2 ... 1
    "arithmetic series"
    Big O notation / approximation:
    O(n^2)
    """
    target_index = 0
    while target_index < len(lst) - 1:
        less_item = None
        less_item_index = None
        for i in range(target_index, len(lst) - 1):
            if less_item is None or item < less_item:
                less_item = item
                less_item_index = i
        else:
            # after list is consumed,
            # swap least value item we "selected" to the top
            tmp = lst[target_index]
            lst[target_index] = less_item
            lst[less_item_index] = tmp
            # next time through,
            # we can skip 1 slot since we know it contains previous least item
            target_index += 1
