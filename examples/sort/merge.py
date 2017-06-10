

class MergeSort(object):

    @classmethod
    def _mergesort_merge(cls, start, end):
        """
        Merge two sorted halves of a list back together
        :param list start: list left half, already sorted
        :param list end: list right half, already sorted
        """
        leftside_end = (start + end) // 2
        rightside_start = leftside_end + 1
        # TODO


    @classmethod
    def _mergesort_recurse(cls, lst, start, end, tmp):
        # sorting is done when we reach a single list element to sort
        if start < end:
            _mergesort_recurse(lst, tmp, start, mid)
            _mergesort_recurse(lst, tmp, mid, end)
            _mergesort_merge(lst, tmp, start, end)

    @classmethod
    def merge(cls, lst):
        """
        Merge sort implementation

        Split the list in half, call merge sort on each half,
        then merge the sorted halves back together.

        Calling merge sort happens recursively.

        From the top frame's perspective, each list half is
        "magically" sorted and then they are merged back together such that the entire list will be sorted.
        Underneath, the list halves have the same thing done to them:
        they are split, sorted, and merged back together.
        So the "magic" sort when looking from the perspective of the most shallow recursive frame,
        is actually merge sort itself.

        On the lowest depth recursive frame,
        we end up with lists containing a single item,
        and that's when we stop calling merge sort / stop recursing.

        The splitting is done inline, by index,
        rather than creating new lists for each half, each time.
        """
        start = 0
        end = len(lst) - 1
        tmp = []
        _mergesort_recurse(lst, tmp, start, end)
