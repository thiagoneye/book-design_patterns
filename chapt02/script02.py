"""
Lazy Instantiation
"""

# Class

class Singleton:
    """
    Lazy instantiation in Singleton pattern.
    """
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(' __init__ method called..')
        else:
            print('Instance already created:', self.get_instance())

    @classmethod
    def get_instance(cls):
        """
        Object creation.
        """
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# Main

if __name__ == '__main__':
    s = Singleton()
    print('Object created', Singleton.get_instance())

    s1 = Singleton()
