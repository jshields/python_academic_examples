#!/usr/bin/env python
"""
based on:
https://stackoverflow.com/a/1894371/3538313

global vars don't work as expected (prints same thread name twice), not thread safe
"""
from time import sleep
from random import random
from threading import Thread


def print_thread_name():
    global v
    print("I'm called from", v)


class T(Thread):
    def run(self):
        global v
        sleep(random())
        v = self.getName()   # Thread-1 and Thread-2 accordingly
        sleep(1)
        print_thread_name()

if __name__ == '__main__':
    print('Thread names do not print as expected, global variable is not thread safe:')
    thread1 = T()
    thread1.start()
    thread2 = T()
    thread2.start()
