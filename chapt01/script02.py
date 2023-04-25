"""
Inheritance 
"""

# Classes

class A:
    def a1(self):
        print("a1")

class B(A):
    def b(self):
        print("b")


# Main

if __name__ == '__main__':
    b = B()
    b.a1()
