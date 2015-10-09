#!/bin/python
# jshields
# this file does not currently contain "tests" for these classes, it just makes sure they kinda work
import logging
from shields.basic_oo_example.animal import Animal  #, Dog, Cat

bigfoot = Animal("Bigfoot", "brown")

print("Here is: %s" % bigfoot)