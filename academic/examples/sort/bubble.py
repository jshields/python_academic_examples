
def bubble_sort(lst):
    """Bubble sort implementation"""
    swapping = True
    while swapping:
        swapping = False
        # because we look-ahead by 1 index, only iterate to length - 1
        for i in range(len(lst) - 1):
            # bigger/greater items should "bubble" to the top
            # if one item belongs where the other is,
            # swap them as part of the sort
            if lst[i] > lst[i + 1]:
                swapping = True
                # swap the items
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp
    return lst
