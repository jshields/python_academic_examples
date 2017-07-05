"""implementations of quicksort"""
import logging

logging.basicConfig(filename='quick_sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


class QuickSort(object):
    """Implementation 1: first element pivot"""

    @classmethod
    def _quicksort_partition(cls, lst, start, end):
        """
        Internal partition and sorting method for quicksort.
        Original C.A.R Hoare quicksort partition scheme implementation.
        https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
        """
        # the pivot element value will be the basis for comparison in sorting
        # we use the first item in this partition of the list as the pivot

        # this is the pivot value
        pivot = lst[start]
        # for now the pivot element remains in its initial list position,
        # and elements following it will be index swapped (their indices switch)
        # relative to the pivot value, not the pivot's index

        # set the starting positions of the left and right brackets
        left = start + 1
        right = end

        # keep swapping until the brackets pass/overlap each other
        swapping = True
        while swapping:
            # relative to the pivot value,
            # left bracket moves from left to right, and will trip on any element with a value not less than,
            # right bracket moves from right to left, and will trip on any element with a value not greater than
            while left <= right and lst[left] <= pivot:
                left = left + 1
            while lst[right] >= pivot and right >= left:
                right = right - 1

            if right < left:
                swapping = False
            else:
                # swap places if the bracket trips
                logging.debug('_quicksort_partition swapping: %s with %s' % (lst[left], lst[right]))
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp
        # swap pivot with the last known right bracket (greater than) element
        # this puts the pivot in between the elements that were swapped to the "less than" position
        # and elements that were swapped to the "greater than" position
        logging.debug('_quicksort_partition final swap: %s with %s' % (lst[start], lst[right]))
        tmp = lst[start]
        lst[start] = lst[right]
        lst[right] = tmp
        # the end result is that all elements less than are left of the pivot element, potentially unsorted
        # and all elements greater than the pivot element are right of the pivot element, potentially unsorted
        # return the pivot index, so that the less than and greater than sides can be partitioned and sorted again,
        # in Sort._quick
        logging.debug('pivot is %s' % right)
        return right

    @classmethod
    def _quick(cls, lst, start, end):
        """Quicksort implementation for a list, internal method"""
        # this method is called recursively
        # on the left and right sections of each partition
        # the sorting work is done in _quicksort_partition

        # eventually, a recursion depth will be reached
        # at which the overall list is fully sorted
        if start < end:
            # sort before and after the pivot
            pivot_index = cls._quicksort_partition(lst, start, end)
            cls._quick(lst, start, pivot_index - 1)
            cls._quick(lst, pivot_index + 1, end)
        return lst

    @classmethod
    def quick(cls, lst, start=0, end=None):
        """
        wrapper method
        """
        logging.debug('quicksort starting: %s' % lst)
        if end is None:
            end = (len(lst) - 1)
        return cls._quick(lst, start, end)


class QuickSortMiddlePivot(QuickSort):
    """
    Implementation 2: middle pivot

    We use the middle element as the pivot,
    to avoid O(n^2) performance in some common scenarios.
    More discussion here:
    https://stackoverflow.com/questions/164163/quicksort-choosing-the-pivot
    https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
    "median of three" pivot selection is also good
    """

    @classmethod
    def _swap(cls, lst, a, b):
        tmp = lst[a]
        lst[a] = lst[b]
        lst[b] = tmp

    @classmethod
    def _quick(cls, lst, left, right):
        """
        Quicksort implementation for a list, internal recursive method
        :param int start: lefthand bounds of list to be partitioned / sorted
        :param int end: righthand bounds of list to be partitioned / sorted
        """

        if left >= right:
            if left == right:
                logging.debug('single element partition: %s' % lst[left])
            # we're at the deepest useful recursion depth, so stop for this branch
            return

        # save initial indices, we'll need them later for partitioning
        left_init = left
        right_init = right

        logging.debug('left: %d, right: %d' % (left, right))
        pivot_index = left + right // 2
        # should this be: pivot_index = left + (right-left) // 2 to avoid going out of range?
        logging.debug('pivot index: %s' % pivot_index)

        pivot_value = lst[pivot_index]
        logging.debug('pivot value: %s' % pivot_value)

        while left <= right:

            # with comparisons relative to the pivot,
            # "left pointer" index moves from left to right, and will stop...
            # "right pointer" index moves from right to left, and will stop...

            while lst[left] <= pivot_value:  # note "equals pivot" included here
                left += 1
            while lst[right] > pivot_value:
                right -= 1

            if left <= right:
                # swap
                logging.debug('before swap: %s' % lst)
                logging.debug('swapping: %s with %s' % (lst[left], lst[right]))

                cls._swap(lst, left, right)

                logging.debug('after swap: %s' % lst)

                # do we need to increment left and right one last time after swap?

        logging.debug(
            'partition/recurse\n'
            'left:\n'
            '%s\n'
            'right:\n'
            '%s' % (
                lst[left_init:right], lst[left:right_init]
            )
        )


        """
        maximum recursion depth exceeded

        (Pdb) lst
        [0, 1, 3, 2, 4, 7, 7, 6, 9]
        (Pdb) right
        4
        (Pdb) right_init
        4
        (Pdb) left
        5
        (Pdb) left_init
        2

        (Pdb) pivot_index
        4
        (Pdb) pivot_value
        4
        """
        try:
            # if left_init < right:
            cls._quick(lst, left_init, right)
            # if left < right_init:
            cls._quick(lst, left, right_init)
        except:
            import pdb;pdb.set_trace()

        return lst
