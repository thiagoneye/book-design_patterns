"""
Singleton Monostate (Borg)
"""

# Class

class Borg:
    """
    Implementation of the Singleton Monostate (Borg) pattern.
    """
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


# Main

if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4

    print("Borg Object 'b': ", b)
    print("Borg Object 'b1': ", b1)
    print("Object State 'b': ", b.__dict__)
    print("Object State 'b1': ", b1.__dict__)
