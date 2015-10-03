#!/bin/python

import logging

from animal import Animal
from dog import Dog
from cat import Cat
from algorithm import Sort, Search
from data_structures import *

#zoo = LinkedList.assemble_from_python_list( [Dog('', '', ''), Cat()] )


# log to a file, with timestamps, including all log levels
logging.basicConfig(filename='utils.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
"""
DEBUG	
INFO	
WARNING	
ERROR	
CRITICAL
"""
logging.info("Main started.");
