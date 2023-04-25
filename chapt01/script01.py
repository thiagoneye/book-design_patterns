"""
Methods
"""

# Class

class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person (%s, %s)>" % (self.name, self.age)


# Main

if __name__ == '__main__':
    p = Person("John", 32)
    print("Type of Object:", type(p), "Memory Address:", id(p))
