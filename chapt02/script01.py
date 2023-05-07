"""
Classic Singleton
"""

# Class

class Singleton:
    """
    Classic implementation of the Singleton pattern.
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# Main

if __name__ == '__main__':
    s = Singleton()
    print('Object created', s)

    s1 = Singleton()
    print('Object created', s1)
