"""
1. Instance Methods

Operate on an instance of the class and have access to the instance (self) and its attributes.
Automatically take the instance as the first argument (conventionally named self).
"""

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}", self)


john = Person("John")
john.greet()

"""
2. Class Methods

Operate on the class itself rather than instances of the class.
Use the @classmethod decorator.
Automatically take the class as the first argument (conventionally named cls).
Can modify class state that applies across all instances of the class.
"""

class Developer(Person):
    @classmethod
    def improve_constantly(cls):
        print("improving constantly", cls)

Developer.improve_constantly()


"""
3. Static Methods

Do not operate on the instance or class. They're bound to the class rather than its object.
Use the @staticmethod decorator.
Do not take a default first argument (neither self nor cls).
Behave like plain functions but belong to the class's namespace.
"""

class Utils:
    @staticmethod
    def fah_to_cel(fah):
        return (fah - 32) * 5 / 9
    
print(Utils.fah_to_cel(70))


"""
4. Abstract Methods

Declared in a base class but intended to be implemented by subclasses.
This concept is central to achieving polymorphism and designing an interface for a group of subclasses.
Use the @abstractmethod decorator from the abc (Abstract Base Classes) module.
Makes a class abstract, meaning it cannot be instantiated on its own, and a subclass must implement the abstract methods.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):                         # implemented in subclass
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                         # implemented in subclass
        return 3.14 * (self.radius ** 2)
    
rectangle = Rectangle(4, 3)
circle = Circle(2.5)

print(rectangle.area())
print(circle.area())

"""
5. Magic/Dunder Methods:

Special methods that begin and end with double underscores (__).
Enable classes to implement and customize behavior with Python's built-in operations. 
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
p = Point(2, 5)
print(p)

"""
6. Property Methods:

Use the @property decorator to make a method callable as an attribute.
Allow for controlled access to attributes, usually to implement getters and setters.
Can be used with @<property_name>.setter to define a setter method for the property.
"""

class BankAccount:
    def __init__(self, deposit):
        self._deposit = deposit     # making it private
        self._interest_rate = 0.08

    @property
    def deposit(self):            # call obj.deposit instead of obj.deposit()
        return self._deposit
    
    @property
    def annual_interest(self):
        return self._deposit * self._interest_rate
    
    @deposit.setter
    def deposit(self, value):
        if value <= 0:
            raise ValueError("Deposit must be positive")
        self._deposit = value


mark = BankAccount(1000)
print(mark.deposit, mark.annual_interest)
mark.deposit = 2000
print(mark.deposit, mark.annual_interest)