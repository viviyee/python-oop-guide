"""
Class

A class is a blueprint for creating objects. 
It defines the attributes/properties and methods that will be associated with objects created from it.
"""

class Person:
    def __init__(self, name, age):
        self.name = name        # attributes/properties
        self.age = age

    def greet(self):            # method
        print(f"Hello, my name is {self.name}")


# Instances / Objects
person_1 = Person("Anna", 29)
person_2 = Person("Finn", 33) 

person_1.greet()
person_2.greet()

# Accessing Attributes
print(person_1.name)
print(person_2.age)

# Modifying Attributes
person_1.age = 20
print(person_1.age)