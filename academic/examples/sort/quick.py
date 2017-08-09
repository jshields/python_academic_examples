"""implementations of quicksort"""
import logging
import sys

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

        if left > right:
            # raise
            logging.error('left %d greater than right %d' % (left, right))
            import ipdb;ipdb.set_trace()

        if left == right:
            logging.debug('single element partition: %s' % lst[left])
            # we're at the deepest useful recursion depth, so stop for this branch
            return

        # save initial indices, we'll need them later for partitioning
        left_init = left
        right_init = right

        logging.debug('left: %d, right: %d' % (left, right))


        pivot_index = (left + right) // 2
        # possibly should be this?
        # pivot_index = left + (right-left) // 2

        logging.debug('pivot index: %s' % pivot_index)
        pivot_value = lst[pivot_index]
        logging.debug('pivot value: %s' % pivot_value)



        """
        QuickSortMiddlePivot.quick([2,6,1,7,3,2])

        IndexError: list index out of range



        2017-08-08 22:13:20,786 quicksort middle pivot starting: [2, 6, 1, 7, 3, 2]
        2017-08-08 22:13:20,786 left: 0, right: 5
        2017-08-08 22:13:20,786 pivot index: 2
        2017-08-08 22:13:20,786 pivot value: 1
        2017-08-08 22:13:20,787 before swap: [2, 6, 1, 7, 3, 2]
        2017-08-08 22:13:20,787 swapping: 2 with 1
        2017-08-08 22:13:20,787 after swap: [1, 6, 2, 7, 3, 2]
        2017-08-08 22:13:20,787 partition/recurse
        left:
        []  <- left partition empty... is that correct?
        right:
        [6, 2, 7, 3]   <- last item chopped off of right partition, is that causing the IndexError?
        2017-08-08 22:13:20,787 single element partition: 1
        2017-08-08 22:13:20,787 left: 1, right: 5
        2017-08-08 22:13:20,787 pivot index: 3
        2017-08-08 22:13:20,787 pivot value: 7
        """


        while left <= right:



            """

            ipdb> lst
            [1, 6, 2, 7, 3, 2]

            ipdb> left_init
            1
            ipdb> right_init
            5

            ipdb> left
            6
            ipdb> right
            5

            ipdb> pivot_value
            7
            ipdb> pivot_index
            3
            """

            # `<=` for "equal to pivot" case  TODO is it needed?
            # pivot is used as break, so doesn't seem so
            try:
                while lst[left] < pivot_value:
                    left += 1
            except:
                import ipdb;ipdb.set_trace()



            try:
                while lst[right] > pivot_value:
                    right -= 1
            except:
                import ipdb;ipdb.set_trace()



            if left <= right:
                # swap
                logging.debug('before swap: %s' % lst)
                logging.debug('swapping: %s with %s' % (lst[left], lst[right]))

                cls._swap(lst, left, right)

                logging.debug('after swap: %s' % lst)
                # increment left and right again after swap changes list
                left += 1
                right -= 1

        logging.debug(
            'partition/recurse\n'
            'left:\n'
            '%s\n'
            'right:\n'
            '%s' % (
                lst[left_init:(right + 1)], lst[left:(right_init + 1)]
            )
        )


        # sys.setrecursionlimit(sys.getrecursionlimit() * 10)

        """
        retest this:
        [0, 1, 3, 2, 4, 7, 7, 6, 9]
        """
        #try:

        # if left_init < right:
        cls._quick(lst, left_init, right)
        # if left < right_init:
        cls._quick(lst, left, right_init)

        #except Exception as e:
        #    import ipdb;ipdb.set_trace()
        #    logging.error(e)


        return lst

    @classmethod
    def quick(cls, lst, start=0, end=None):
        """
        wrapper method
        """
        logging.debug('quicksort middle pivot starting: %s' % lst)
        if end is None:
            end = (len(lst) - 1)
        return cls._quick(lst, start, end)
