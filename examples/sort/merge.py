"""
TODO iterative bottom-up solution https://en.wikipedia.org/wiki/Merge_sort
"""
import logging

logging.basicConfig(
    filename='merge_sort.log',
    level=logging.DEBUG
)


def _merge_sorted_lists(left_lst, right_lst):
    # credit to https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
    if not left_lst:
        return right_lst
    if not right_lst:
        return left_lst

    left_index = right_index = 0  # use two "pointers" for positions in each input list
    target_length = len(left_lst) + len(right_lst)
    result = []
    while len(result) < target_length:
        if left_lst[left_index] < right_lst[right_index]:
            # left item we point at is less, it goes in first
            result.append(left_lst[left_index])
            left_index += 1
        else:
            result.append(right_lst[right_index])
            right_index += 1

        # check if one of the lists being merged has been exhausted
        if right_index == len(right_lst):
            # if right is exhausted, add in the rest of the left list,
            # starting from its "pointer" `left_index`
            result.extend(left_lst[left_index:])
            break
        elif left_index == len(left_lst):
            # if left is exhausted, add in what's left of the right
            result.extend(right_lst[right_index:])
            break

    logging.debug('Merged {left_lst} and {right_lst}, returning {result}'.format(
        left_lst=left_lst, right_lst=right_lst, result=result))
    return result


def _merge_sort_recurse(lst):
    lst_len = len(lst)

    if lst_len in (0, 1):
        # empty or single item is considered sorted
        return lst

    # find middle
    # (using floored division here is fine)
    mid = lst_len // 2

    # split
    left = lst[:mid]  # slice start to mid (not inclusive)
    right = lst[mid:]  # slice mid to end

    # merge sort left
    left_sorted = _merge_sort_recurse(left)

    # merge sort right
    right_sorted = _merge_sort_recurse(right)

    # merge the halves together
    return _merge_sorted_lists(left_sorted, right_sorted)


def merge_sort(lst):
    return _merge_sort_recurse(lst)
