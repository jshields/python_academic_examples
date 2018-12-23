# python academic examples
Work in Progress

Not meant for practical use; for educational purposes only.

The goal of this repo is to demonstrate concepts, such as what certain alogrithms do,
using Python syntax to keep things simple,
even though the code will maybe be doing things that don't make sense to do in Python.

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
  - Merge Sort :x:
  - Quicksort (Hoare partition scheme) :white_check_mark:
  - Quicksort (middle pivot) :white_check_mark:
  - Insertion Sort :white_check_mark:
  - Selection Sort :white_check_mark:
- search
  - Linear Search :white_check_mark:
  - Binary Search :white_check_mark:


### Running unit tests:
`unittest` CLI from inside package:

    # all tests
    python -m unittest
    # individual test
    python -m unittest tests.test_fibonacci

### `sort` usage:

    from examples.sort.quick import QuickSortMiddlePivot
    QuickSortMiddlePivot.quick([2,6,1,7,3,2])



#### Footnotes:

https://www.hindawi.com/journals/isrn/2012/947634/

http://www.bogotobogo.com/Algorithms/quicksort.php

https://stackoverflow.com/questions/27203462/quicksort-algorithm-with-element-in-the-middle-as-pivot

https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort

http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/quicksort.pdf

http://www.geeksforgeeks.org/quick-sort/
