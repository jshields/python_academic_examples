"""
https://stackoverflow.com/a/13240093/3538313
multiprocessing module
global variables here are thread local,
since the multiprocessing module creates a new process for each thread.

Consider this example, where the processed counter is an example of thread local storage:
"""

from multiprocessing import Pool
from random import random
from time import sleep
import os

counter = 0


def f(x):
    # exaggerate latency, to make it clear order of steps is not guaranteed:
    sleep(random())

    global counter
    counter += 1
    print('Step {x} - Process ID {pid}, counter {count}'.format(
        x=x, pid=os.getpid(), count=counter))

if __name__ == '__main__':
    print(
        'Stepping 0 through 9...\n'
        'Notice each process has a separate thread local counter, '
        'and steps (most likely) finish out of order:'
    )
    pool = Pool(processes=3)
    pool.map(f, range(10))
