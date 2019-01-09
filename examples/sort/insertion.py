import logging
import copy

logging.basicConfig(
    filename='insertion_sort.log',
    format='%(asctime)s %(message)s',
    level=logging.DEBUG
)


def insertion_sort(src_lst, start=0, end=None, inline=False):
    """Insertion sort implementation"""
    # support for inline sorting vs returning a sorted copy
    if inline:
        lst = src_lst
    else:
        lst = copy.deepcopy(src_lst)

    if end is None:
        end = len(lst)

    # because we look-behind by 1 index, start iteration at length + 1
    for i in range(start + 1, end):
        value = lst[i]
        cursor = i - 1

        logging.debug(
            'insertion: looping, index at {ind}, '
            'current value {val}, cursor at {cursor}'.format(
                ind=i,
                val=value,
                cursor=cursor
            )
        )

        # while the elements behind the current element are of greater value,
        # push the current element backwards
        while lst[cursor] > value and cursor >= 0:
            # starting from the element of current 'value',
            # swap values with the element that the cursor is looking back towards,
            # falling through the rest of the list behind the current element
            logging.debug(
                'insertion: while looping, shifting index of {item} up by one'.format(
                    item=lst[cursor]
                )
            )
            lst[cursor + 1] = lst[cursor]
            cursor -= 1
            logging.debug(
                'insertion: while looping, cursor at {cursor}'.format(cursor=cursor)
            )
        # finally, insert the 'value' back into the list
        logging.debug(
            'insertion: out of while, '
            'inserting {item} back into the list at index {ind}'.format(
                item=lst[cursor + 1],
                ind=cursor + 1
            )
        )
        lst[cursor + 1] = value

    return lst
