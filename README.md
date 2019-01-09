# python academic examples
Work in Progress

Not meant for practical use; for educational purposes only.

The goal of this repo is to demonstrate concepts, such as what certain alogrithms do,
using Python syntax to keep things simple,
even though the code will be doing things that don't make sense to do in Python / any real production scenario.

### Contents:

basic Object Oriented example
- Animal :white_check_mark:
- Cat :white_check_mark:
- Dog :white_check_mark:
- Unicode animal emoji methods :white_check_mark:
- associated unit tests :white_check_mark:

algorithms
- sort
  - Bubble Sort :white_check_mark:
  - Merge Sort (recursive) :white_check_mark:
  - Quicksort (Hoare partition scheme) :white_check_mark:
  - Quicksort (middle pivot) :white_check_mark:
  - Insertion Sort :white_check_mark:
  - Selection Sort :white_check_mark:
- search
  - Linear Search :white_check_mark:
  - Binary Search :white_check_mark:

other curiosities:
    - ackermann
    - Fibonacci Sequence (implementations using various approaches)
    - some threading examples.
        May want to move these out into their own repo demonstrating race conditions


### Running unit tests:
`unittest` CLI:

    # all tests
    python -m unittest
    # individual test
    python -m unittest tests.test_fibonacci

### `sort` usage:

    from examples.sort.quick import QuickSortMiddlePivot
    QuickSortMiddlePivot.quick([2,6,1,7,3,2])



#### Footnotes:

https://www.hindawi.com/journals/isrn/2012/947634/
