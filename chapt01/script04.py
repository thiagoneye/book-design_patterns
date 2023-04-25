"""
Composition 
"""

# Classes

class A:
    def a1(self):
        print("a1")

class B(object):
    def b(self):
        print("b")
        A().a1()


# Main

if __name__ == '__main__':
    objectB = B()
    objectB.b()
