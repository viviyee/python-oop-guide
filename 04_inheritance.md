
## Inheritance

Inheritance allows a class (subclass/derived class) to inherit properties/attributes and methods/behavior from another class (superclass/base class).

### Parent Class (Super Class/ Base Class)

```python
class Animal:                   
    def __init__(self, name):
        self.name = name

    def make_sound(self):       
        pass

    def eat(self):
        return "eating~"
```

### Child Class (Sub Class/ Derived Class)

```python
class Dog(Animal):              
    def make_sound(self):           # Method Overriding
        print("woof woof")

    def guard_house(self):          # New method for child class
        print("I am guarding the house")

buddy = Dog("buddy")
buddy.make_sound()                  # woof woof
buddy.guard_house()                 # I am guarding the house
```

### super() function

```python
class Cat(Animal):              
    def make_sound(self):                           # Method Overriding
        print("meow meow")

    def eat(self):                  
        return super().eat() + " cat foods"        # super() function
    

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)                      # super() function
        self.color = color

whiskers = Cat("whiskers")
mr_blue = Bird("mr. blue", "blue")                  
```

### Inheritance Hierarchy

```python
class Bulldog(Dog):
    pass

winston = Bulldog("winston")
winston.make_sound()
winston.guard_house()
```

### Multiple Inheritance
Python also supports multiple inheritance, where a class can inherit attributes and methods from more than one parent class.

```python
class Aquatic:
    def speak(self):
        print("I live in water")

class Mammal:
    def speak(self):
        print("I feed my children milk")

class Whale(Aquatic, Mammal):
    def speak(self):
        super().speak()


beluga = Whale()
beluga.speak()              # I live in water
```

### Method Resolution Order (MRO)
- Python uses the C3 linearization algorithm to determine the method resolution order (MRO) in multiple inheritance. 
- You can access the MRO of a class using the `rmo()` method or the `__mro__` attribute.

```python
print(Whale.mro())

# [<class '__main__.Whale'>, <class '__main__.Aquatic'>, <class '__main__.Mammal'>, <class 'object'>]
```