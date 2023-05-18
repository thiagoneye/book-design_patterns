"""
State Pattern
"""

# Imports

from abc import ABCMeta, abstractmethod


# Classes

class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA")

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB")

class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


# Main

if __name__ == "__main__":
    context = Context()
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()

    context.set_state(state_a)
    context.handle()
