#!/usr/bin/python
"""animal module"""
import logging


logging.basicConfig(
    filename='animal.log',
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
)


class Animal(object):
    """Animal is the base class for animals."""

    _emoji = u'\u2753'  # black-question-mark-ornament
    _sound = '...'

    def __init__(self, name, breed, color):
        self._name = name
        self._breed = breed
        self._color = color

        logging.info('{obj} initialized'.format(obj=self))

    def __repr__(self):
        return '<{class_name} name={name} breed={breed} color={color} >'.format(
            class_name=self.__class__.__name__,
            name=self._name,
            breed=self._breed,
            color=self._color,
        )

    def __str__(self):
        return '{name} the {color} {breed}'.format(
            name=self._name,
            color=self._color,
            breed=self._breed
        )

    def speak(self):
        """
        Speak method should in some way describe the sound an animal makes.
        Children should define their _sound or override.
        """
        try:
            print(self._sound)
            return self._sound
        except AttributeError:
            raise NotImplementedError(
                'No _sound defined for this animal! ({obj})'.format(obj=self)
            )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def emoji(cls):
        """
        Each Animal subclass should set '_emoji' equal to a unicode character
        representing their class
        """
        return cls._emoji
