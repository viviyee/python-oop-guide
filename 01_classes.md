
## Classes

A class is a blueprint for creating objects. 

It defines the attributes/properties and methods/behaviors that will be associated with objects created from it.

```python
class Person:
    def __init__(self, name, age):
        self.name = name        # attributes/properties
        self.age = age

    def greet(self):            # methods/behaviors
        print(f"Hello, my name is {self.name}")
```

## Instances / Objects

An object is an instance of a class.

```python
person_1 = Person("Anna", 29)
person_2 = Person("Finn", 33) 

person_1.greet()
person_2.greet()
```

## Privacy

__Public__: In Python, all attributes and methods are public by default, meaning they can be accessed from outside the class.

```python
# Accessing Attributes
print(person_1.name)
print(person_2.age)

# Modifying Attributes
person_1.age = 23
print(person_1.age)
```