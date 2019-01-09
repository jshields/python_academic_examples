#!/usr/bin/python

from examples.basic_oo_example.animal import Animal


class Cat(Animal):
    """Cat class, child of Animal"""

    _emoji = u'\U0001F431'  # cat-face
    _sound = 'Meow!'  # used by Animal's speak method

    def scratch(self, target):
        result = '{animal_name} the cat scratches {target}'.format(
            animal_name=self.name,
            target=str(target)
        )
        print(result)
        return result
