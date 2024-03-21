"""
1. Instance Variables

Also known as object attributes.
Each instance of a class (object) has its own copy of instance variables.
Defined within methods using the self keyword.
Accessible using dot notation (object.variable).
Instance variables hold data unique to each object.
"""

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

noah = Person("noah", "noah@gmail.com")
print(noah.name, noah.email)


"""
2. Class Variables

Also known as class attributes or static variables.
Shared among all instances of a class.
Defined outside of any method in the class scope.
Accessible using dot notation (Classname.variable or object.variable).
"""

class Chicken:
    count = 0

    def __init__(self, name):
        self.name = name
        Chicken.count += 1

    def die(self):
        del self
        Chicken.count -= 1

    @classmethod
    def buy_chickens(cls, n):
        cls.count += n

    @classmethod
    def sell_chickens(cls, n):
        cls.count -= n


heihei = Chicken("heihei")
Chicken.buy_chickens(50)
Chicken.sell_chickens(20)
print(Chicken.count)


"""
Private and Public

In Python, unlike some other programming languages like C++ or Java, there is no strict enforcement of private or public access modifiers at the class level. 
However, Python provides a convention to indicate the visibility of class members. 
These conventions are followed by programmers to indicate the intended use of attributes and methods, but they can still be accessed and modified from outside the class if necessary.
"""

class Public:
    def __init__(self, abc, xyz):
        self.abc = abc
        self.xyz = xyz
        self._private = "I am private :("

    def display(self):
        print(f"Public (abc: {self.abc}, xyz: {self.xyz})")

    def _display(self):
        print(f"Private (abc: {self.abc}, xyz: {self.xyz})")


p = Public("123", "JQK")
print(p.abc, p.xyz, p._private)
p.display()
p._display()