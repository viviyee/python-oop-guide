
## Attributes

### Instance Attributes
- Attributes that belong to each individual object.
- They are defined within methods of the class, usually within the __init__ method.
- Instance attributes are accessed and modified using dot notation (`object.attribute_name`).

```python
class Student:
    def __init__(self, grade):
        self.grade = grade


student = Student("B")
print(student.grade)
```

### Class Attributes
- Class attributes are shared by all instances of the class.
- They are defined outside of any methods in the class definition.
- Class attributes are accessed using the class name itself or an instance of the class.
- To declare a class attribute, you simply assign a value to a variable within the class definition.

```python
class Person:
    population = 0

    def __init__(self):
        Person.population += 1


person_1 = Person()
person_2 = Person()
person_3 = Person()

print(Person.population)
print(person_1.population)
```