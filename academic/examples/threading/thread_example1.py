"""
Based on this answer:
https://www.quora.com/Are-local-variables-in-a-python-function-thread-safe

Local variables are certainly "thread-exclusive."
No other thread can access them directly,
and this is helpful but not sufficient to guarantee semantic thread safety.

A local variable in one thread does not store its value
in the same location as the same-named local variable in another thread.

This is basically a direct consequence of the definition of functions and local variables.
More or less every structured programming language does something like the following:
Every time a function is invoked, a new block of memory called a stack frame is allocated
(and it becomes invalid/destroyed when the function returns).
Local variables' values are stored within that stack frame.

So, in Python, you can have two (or more) copies of this function running
in separate threads,
and the values of a, b, c in each thread will refer to distinct objects:
    def func():
        # create local variables a, b, c
        # do stuff with local variables a, b, c
        return

However, guaranteeing that two threads have separate storage for local variables
is not enough to ensure thread-safety,
because those local variables can refer to globally shared data in a thread-unsafe way.

For example, try running the following code.
You'll see that the output list contains integers 0-9 in an apparently non-deterministic.
Each of the 20 threads gets its own local variable lst,
as proven by the statement on line 7,
but they all actually refer to the same shared object!
"""
import threading
import time


def append_integers(lst, start, stop):
    time.sleep(1)
    for x in range(start, stop):
        lst.append(x)
    lst = None  # doesn't affect other threads' lst variable

output_lst = []
threads = []
for ii in range(20):
    th = threading.Thread(target=append_integers, args=(output_lst, 0, 10))
    th.start()
    threads.append(th)

print('Output in main thread before joining threads:', output_lst)

# threads need to be joined for output list to contain anything as seen by standard out,
# without this it's an empty list `[]`
for th in threads:
    th.join()

print('Output after joining threads, we can see the list object was shared:', output_lst)
