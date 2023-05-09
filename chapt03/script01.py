"""
Simple Factory Pattern
"""

# Imports

from abc import ABCMeta, abstractmethod


# Class

class Animal(metaclass = ABCMeta):
    """
    Superclass
    """
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    """
    Subclass
    """
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    """
    Subclass
    """
    def do_say(self):
        print("Meow Meow!!")

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


# Main

if __name__ == '__main__':
    ff = ForestFactory()

    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
