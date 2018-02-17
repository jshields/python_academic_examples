#!/usr/bin/env python
"""
based on:
https://stackoverflow.com/a/1894371/3538313
"""

from time import sleep
from random import random
from threading import Thread, local

# threadlocal data is thread safe, works as expected
data = local()


def print_thread_name():
    print("I'm called from", data.v)


class T(Thread):
    def run(self):
        sleep(random())
        data.v = self.getName()  # Thread-1 and Thread-2 accordingly
        sleep(1)
        print_thread_name()

if __name__ == '__main__':
    print('Thread names print as expected, handled in a thread safe way:')
    thread1 = T()
    thread1.start()
    thread2 = T()
    thread2.start()
