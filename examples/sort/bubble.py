
def bubble_sort(lst):
    """
    Bubble sort implementation
    Naive sorting algorithm

    Each of the n items could take n-1 (all other items) comparisons in worst case,
    n * (n-1) = n^2 - n = O(n^2) time complexity performance.

    When we've performed a swap,
    on the next pass i will point to where that element now is,
    meaning that we continue "bubbling" that element up
    for as long as there is an item less than it in front (they are out of order).

    Otherwise, if no swap was performed, i simply moves on to look for an item that
    needs to be swapped.

    When the loop finishes without finding any item that needs to be swapped,
    the whole list must be sorted.
    """
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


# TODO test this, then add the next optimization
def bubble_sort_optimized(lst):
    """
    Bubble sort is not efficient,
    so optimizing it doesn't help as much as switching algorithms,
    but let's do it anyway.

    > The bubble sort algorithm can be easily optimized
    > by observing that the n-th pass finds the n-th largest element
    > and puts it into its final place.
    > So, the inner loop can avoid looking at the last n - 1 items
    > when running for the n-th time
    https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort

    We will swap an element for as long as the next element is lesser than.

    First, the largest element will bubble to the top.
    While we won't necessarily start on the largest item,
    we can see that after the first pass of the inner loop,
    the largest item is in its final position.

    [2, 1, 3, 8, 5, 4] -> [1, 2, 3, 8, 5, 4] 2 > 1
    [1, 2, 3, 8, 5, 4] -> [1, 2, 3, 5, 8, 4] 8 > 5
    [1, 2, 3, 5, 8, 4] -> [1, 2, 3, 5, 4, 8] 8 > 4
    [1, 2, 3, 5, 4, 8] -> [1, 2, 3, 5, 4, 8] no change, done

    Now that the largest element is at index n, we know it's in the right place
    and only need to check up to n-1 next time, in the case of i being 1.
    This pattern continues as we loop through to n-i-1 as i is incremented.
    (extra -1 accounts for the fact that
    we check the element in front of the one we're swapping)

    The next optimization after the one above is to also break if no swap in inner loop:
    https://www.geeksforgeeks.org/bubble-sort/

    However, an optimization that subsumes this optimization is possible next:
    "after every pass, all elements after the last swap are sorted, and do not need to be checked again"
    TODO skip over already swapped elements on the next pass by setting `newn`
    """
    n = len(lst)

    # for every slot in the list
    for i in range(n):

        # bubble the n-th biggest item into position
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
