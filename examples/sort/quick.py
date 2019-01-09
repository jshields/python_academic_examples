"""
implementations of quicksort


http://www.bogotobogo.com/Algorithms/quicksort.php

https://stackoverflow.com/questions/27203462/quicksort-algorithm-with-element-in-the-middle-as-pivot

https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort

http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/quicksort.pdf

http://www.geeksforgeeks.org/quick-sort/

"""
import logging

logging.basicConfig(
    filename='quick_sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG
)


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
            """
            relative to the pivot value,
            left bracket moves from left to right,
            and will trip on any element with a value not less than,
            right bracket moves from right to left,
            and will trip on any element with a value not greater than
            """
            while left <= right and lst[left] <= pivot:
                left = left + 1
            while lst[right] >= pivot and right >= left:
                right = right - 1

            if right < left:
                swapping = False
            else:
                # swap places if the bracket trips
                logging.debug(
                    '_quicksort_partition swapping: {left_item} with {right_item}'.format(
                        left_item=lst[left],
                        right_item=lst[right]
                    )
                )
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp
        """
        swap pivot with the last known right bracket (greater than) element
        this puts the pivot in between
        the elements that were swapped to the "less than" position
        and elements that were swapped to the "greater than" position
        """
        logging.debug(
            '_quicksort_partition final swap: '
            'pivot {pivot_item} with {right_item}'.format(
                pivot_item=lst[start],
                right_item=lst[right]
            )
        )
        tmp = lst[start]
        lst[start] = lst[right]
        lst[right] = tmp
        """
        the end result is that all elements less than are left of the pivot element,
        potentially unsorted,
        and all elements greater than the pivot element are right of the pivot element,
        potentially unsorted,
        return the pivot index,
        so that the less than and greater than sides can be partitioned and sorted again,
        in `Sort._quick`
        """
        logging.debug('pivot index is {right}'.format(right=right))
        return right

    @classmethod
    def _quick(cls, lst, start, end):
        """Quicksort implementation for a list, internal method"""
        """
        this method is called recursively
        on the left and right sections of each partition
        the sorting work is done in `_quicksort_partition`.
        eventually, a recursion depth will be reached
        at which the overall list is fully sorted
        """
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
        logging.debug('quicksort starting: {lst}'.format(lst=lst))
        if end is None:
            end = (len(lst) - 1)
        return cls._quick(lst, start, end)


class QuickSortMiddlePivot(object):
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
            logging.debug('single element partition: {item}'.format(item=lst[left]))
            # we're at the deepest useful recursion depth, stop partitioning
            # returning the list here makes it work for 1 item lists
            return lst

        # save initial indices, we'll need them later for partitioning
        left_init = left
        right_init = right

        logging.debug('left: {left}, right: {right}'.format(left=left, right=right))

        pivot_index = (left + right) // 2
        # Could be this to prevent integer overflow:
        # pivot_index = left + (right-left) // 2

        logging.debug('pivot index: {ind}'.format(ind=pivot_index))
        pivot_value = lst[pivot_index]
        logging.debug('pivot value: {val}'.format(val=pivot_value))

        """
        sometimes elements are swapped with themselves,
        is there a way to skip this without getting stuck in a loop?
        E.g. [2,6,1,7,7,7,7,3,2] -> swap 6 with 6
        """
        while left <= right:

            # pivot is used as while loop break
            while lst[left] < pivot_value:
                left += 1
            while lst[right] > pivot_value:
                right -= 1

            if left <= right:
                # swap
                logging.debug('before swap: {lst}'.format(lst=lst))
                logging.debug('swapping: {left_item} with {right_item}'.format(
                        left_item=lst[left],
                        right_item=lst[right]
                    )
                )

                cls._swap(lst, left, right)

                logging.debug('after swap: {lst}'.format(lst=lst))
                # increment left and right again after swap changes list
                left += 1
                right -= 1

        logging.debug(
            'partition/recurse\n'
            'left:\n'
            '{left}\n'
            'right:\n'
            '{right}'.format(
                left=lst[left_init:(right + 1)],
                right=lst[left:(right_init + 1)]
            )
        )

        # May need iterative approach for larger lists due to recursion limit
        # Recursion limit can be increased but not ideal for stack size/speed:
        # sys.setrecursionlimit(sys.getrecursionlimit() * 10)

        cls._quick(lst, left_init, right)
        cls._quick(lst, left, right_init)

        return lst

    @classmethod
    def quick(cls, lst, start=0, end=None):
        """
        wrapper method
        """
        logging.debug('quicksort middle pivot starting: {lst}'.format(lst=lst))
        if end is None:
            end = (len(lst) - 1)
        return cls._quick(lst, start, end)
