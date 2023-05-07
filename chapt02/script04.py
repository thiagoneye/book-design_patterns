"""
Singleton Monostate (Borg)
"""

# Class

class Borg:
    """
    Implementation of the Singleton Monostate (Borg) pattern.
    """
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


# Main

if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b1.x = 1

    print("Borg Object 'b': ", b)
    print("Borg Object 'b1': ", b1)
    print("Object State 'b': ", b.__dict__)
    print("Object State 'b1': ", b1.__dict__)
