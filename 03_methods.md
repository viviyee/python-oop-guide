
## Methods

### Instance Methods
- They operate on an instance of the class and have access to instance attributes through the `self` parameter.
- They can modify instance state and are commonly used for tasks that involve the instance's data.
- Instance methods are defined without any special decorators.

```python
class Country:
    def __init__(self, capital):
        self.capital = capital

    def set_new_capital(self, new_capital):
        self.capital = new_capital


japan = Country("Kyoto")
japan.set_new_capital("Tokyo")
print(japan.capital)                # Tokyo
```

### Class Methods
- Class methods operate on the class itself rather than instances.
- They have access to class variables and can modify class state through the `cls` parameter.
- They are defined using the `@classmethod` decorator.
- Class methods are often used for factory methods or methods that need to access or modify class-level attributes.

```python
class BankAccount:
    interest = 0.07         # 7 percent

    def __init__(self, deposit):
        self.deposit = deposit

    def display_interest(self):
        print(self.deposit * BankAccount.interest)

    @classmethod
    def update_interest(cls, new_interest):
        cls.interest = new_interest


acc_1 = BankAccount(1000)
acc_1.display_interest()                # 70.0

BankAccount.update_interest(0.08)       # 8 percent now
acc_1.display_interest()                # 80.0
```

### Static Methods
- Static methods are not bound to the instance or the class. 
- They behave like regular functions but are defined within a class for __organization purposes__.
- They cannot access or modify instance or class state and do not have access to `self` or `cls`.
- They are defined using the `@staticmethod` decorator.
- Static methods are often used for utility functions that are related to the class but do not require access to instance or class attributes.

```python
class Student:
    @staticmethod
    def search_scholarships():
        print("Searching available scholarships...")

Student.search_scholarships()
```