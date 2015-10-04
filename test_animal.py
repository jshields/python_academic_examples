#!/bin/python
# jshields
# TODO make this contain real unit tests rather than debugging smoke tests
import logging
from shields.basic_oo_example.animal import Animal
from shields.basic_oo_example.dog import Dog
from shields.basic_oo_example.cat import Cat

zoo = []

# Animal
bigfoot = Animal('Bigfoot', 'unknown', 'brown')
zoo.append(bigfoot)

# Dog
rover = Dog('Rover', 'Great Dane', 'grey')
zoo.append(rover)

# Cat
whiskers = Cat('Whiskers', 'Tabby', 'orange')
zoo.append(whiskers)

for a in zoo:
	print(a)
