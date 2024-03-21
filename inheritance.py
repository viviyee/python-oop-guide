"""
Inheritance:

Inheritance allows a class (subclass/derived class) to inherit properties/attributes and methods/behavior from another class (superclass/base class).
"""

# Super class / Base class
class Animal:                   
    def __init__(self, name):
        self.name = name

    def make_sound(self):       
        pass

    def eat(self):
        return "eating~"


# Sub class / Derived Class
class Dog(Animal):              
    def make_sound(self):           # Method Overriding
        print("woof")

    def guard_house(self):
        print("I am guarding the house")


# Sub class access to super class
class Cat(Animal):              
    def make_sound(self):           # Method Overriding
        print("meow")

    def eat(self):                  
        return super().eat() + " cat foods"        # Access to super class
    

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)                      # Access to super class
        self.color = color



buddy = Dog("buddy")
whiskers = Cat("whiskers")
blue = Bird("blue", "blue")                         # Bird takes 2 arg

buddy.make_sound()
buddy.guard_house()

whiskers.make_sound()
print( whiskers.eat() )


# Inheritance Hierarchy
class Bulldog(Dog):
    pass


winston = Bulldog("winston")
winston.make_sound()
print( winston.eat() )


