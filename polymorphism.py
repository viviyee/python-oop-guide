"""
Polymorphism

Polymorphism allows methods to do different things based on the object that calls them. 
In Python, this is achieved through method overriding and method overloading.
"""

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("woof")

class Cat(Animal):
    def make_sound(self):
        print("meow")


# Polymorphism in action
# The same function behaves differently based on the type of object passed to it.
def make_animal_sound(animal):      # takes animal object as an arg
    animal.make_sound()


dog = Dog()
cat = Cat()

make_animal_sound(dog)
make_animal_sound(cat)


# Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"Point ({self.x}, {self.y})"
    
    # get length from origin (0, 0)
    def hypotenuse(self):
        import math
        return round(math.sqrt(self.x**2 + self.y**2), 4)
    
    def __gt__(self, other):
        return self.hypotenuse() > other.hypotenuse()
        
    def __ge__(self, other):
        return self.hypotenuse() >= other.hypotenuse()
    
    def __lt__(self, other):
        return self.hypotenuse() < other.hypotenuse()
    
    def __le__(self, other):
        return self.hypotenuse() <= other.hypotenuse()
        
    def __eq__(self, other):
        return self.hypotenuse(), 2 == other.hypotenuse(), 2
    

point_1 = Point(1, 3)
point_2 = Point(5, 6)

point_3 = point_1 + point_2
point_4 = point_1 - point_2

print(point_3)               # Point (6, 9)
print(point_4)               # Point (-4, -3)

print("p1 > p2", point_1 > point_2)
print("p1 >= p2", point_1 >= point_2)
print("p1 < p2", point_1 < point_2)
print("p1 <= p2", point_1 <= point_2, point_1.hypotenuse(), point_2.hypotenuse())
print("p1 == p2", point_1 == point_2, point_1.hypotenuse(), point_2.hypotenuse())

point_5 = Point(-1, -3)
print("p1 == p5", point_1 == point_5, point_1.hypotenuse(), point_5.hypotenuse())


"""
Arithmetic Operators:

    __add__(self, other) for addition (+)
    __sub__(self, other) for subtraction (-)
    __mul__(self, other) for multiplication (*)
    __truediv__(self, other) for division (/)
    __floordiv__(self, other) for floor division (//)
    __mod__(self, other) for modulus (%)
    __pow__(self, other[, modulo]) for exponentiation (**)

Comparison Operators:

    __lt__(self, other) for less than (<)
    __le__(self, other) for less than or equal to (<=)
    __eq__(self, other) for equality (==)
    __ne__(self, other) for not equal (!=)
    __gt__(self, other) for greater than (>)
    __ge__(self, other) for greater than or equal to (>=)

Unary Operators:

    __neg__(self) for negation (-)
    __pos__(self) for unary plus (+)
    __abs__(self) for absolute value (abs())
    __invert__(self) for bitwise inversion (~)

Type Conversion:

    __int__(self) for int()
    __float__(self) for float()
    __complex__(self) for complex()
    __str__(self) for str()
    __repr__(self) for repr()
    __bytes__(self) for bytes()
    __bool__(self) for bool()

Container Methods:

    __len__(self) for len()
    __getitem__(self, key) for getting an item by index or key
    __setitem__(self, key, value) for setting an item by index or key
    __delitem__(self, key) for deleting an item by index or key
"""


