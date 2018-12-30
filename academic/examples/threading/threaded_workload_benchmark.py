"""
WIP

Based on:
http://chriskiehl.com/article/parallelism-in-one-line/
"""
import timeit
import urllib2

# starts a new process for each worker,
# parallel
from multiprocessing import Pool as ProcessPool

# multiple threads but all subject to the GIL,
# concurrent but not parallel
from multiprocessing.dummy import Pool as ThreadPool


urls = [
    'http://www.github.com',
    'http://www.google.com',
    'http://stackoverflow.com',
]


def serial_network_bound_work():
    results = map(urllib2.urlopen, urls)
    return results


def processed_network_bound_work():
    # Make the Pool of workers
    pool = ProcessPool(4)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib2.urlopen, urls)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()
    return results


def threaded_network_bound_work():
    # Make the Pool of workers
    pool = ThreadPool(4)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib2.urlopen, urls)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()
    return results


# TODO
def processed_cpu_bound_work():
    pass


def threaded_cpu_bound_work():
    pass


if __name__ == '__main__':
    def benchmark(func):
        func_name = func.name
        print(timeit.timeit(
            '{func_name}()'.format(func_name=func_name),
            setup='from __main__ import {func_name}'.format(func_name=func_name)
        ))

    map(benchmark, [
        serial_network_bound_work,
        processed_network_bound_work,
        threaded_network_bound_work,
        processed_cpu_bound_work,
        threaded_cpu_bound_work,
    ])
