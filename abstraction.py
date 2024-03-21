"""
Abstraction:
Abstraction involves hiding the complex implementation details and showing only the essential features of the object. In Python, abstraction is implemented using abstract classes and methods.
"""

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
print(dog.sound())  # Output: Woof!

cat = Cat()
print(cat.sound())  # Output: Meow!