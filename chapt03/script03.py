"""
Abstract Factory Pattern
"""

# Imports

from abc import ABCMeta, abstractmethod


# Class

class PizzaFactory(metaclass = ABCMeta):
    """
    Superclass
    """
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    """
    Subclass
    """
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory):
    """
    Subclass
    """
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()

class VegPizza(metaclass = ABCMeta):
    """
    Superclass
    """
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass = ABCMeta):
    """
    Superclass
    """
    @abstractmethod
    def serve(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):
    """
    Subclass
    """
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
    """
    Subclass
    """
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ",
              type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    """
    Subclass
    """
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
    """
    Subclass
    """
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on",
              type(VegPizza).__name__)

class PizzaStore:
    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


# Main

if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizzas()
